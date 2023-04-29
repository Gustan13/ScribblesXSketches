import pygame

from tile import Tile
from explosion import Explosion

from settings import TILE_SIZE
from toolbox import check_group_positions, round_to_multiple_nearest


class Bomb(Tile):
    def __init__(self, pos, groups, obstacle_sprites, explosion_sprites, player):
        super().__init__(pos, groups, "bomb.png")

        self.timer = 100
        self.is_dead = False
        self.player = player

        self.speed = 0
        self.direction = pygame.math.Vector2()

        self.obstacle_sprites = obstacle_sprites
        self.explosion_sprites = explosion_sprites

        self.can_kick = False
        self.can_collide_with_player = False

    def explode_path(self, row, col, size):
        """Explodes a path of tiles in the four directions."""
        aux = 1

        Explosion((col, row), [self.explosion_sprites])

        # explode to the right
        while (
            not check_group_positions(
                (col + TILE_SIZE * aux, row), self.obstacle_sprites
            )
        ) and (aux <= size):
            Explosion((col + TILE_SIZE * aux, row), [self.explosion_sprites])
            aux += 1

        aux = 1

        # explode to the left
        while (
            not check_group_positions(
                (col - TILE_SIZE * aux, row), self.obstacle_sprites
            )
        ) and (aux <= size):
            Explosion((col - TILE_SIZE * aux, row), [self.explosion_sprites])
            aux += 1

        aux = 1

        # explode down
        while (
            not check_group_positions(
                (col, row + TILE_SIZE * aux), self.obstacle_sprites
            )
        ) and (aux <= size):
            Explosion((col, row + TILE_SIZE * aux), [self.explosion_sprites])
            aux += 1

        aux = 1

        # explode up
        while (
            not check_group_positions(
                (col, row - TILE_SIZE * aux), self.obstacle_sprites
            )
        ) and (aux < size + 1):
            Explosion((col, row - TILE_SIZE * aux), [self.explosion_sprites])
            aux += 1

        return

    def explosion_collision(self):
        """Checks collision with explosions"""
        explosions_hit = pygame.sprite.spritecollide(
            self, self.explosion_sprites, False
        )

        if explosions_hit:
            self.timer = 0

    def update_can_kick(self):
        """Checks if the bomb can be kicked"""
        # if not on the same tile as the player, can kick
        if pygame.sprite.spritecollide(self, [self.player], False):
            self.can_kick = False
        else:
            self.can_collide_with_player = True
            self.can_kick = True

    def kick(self):
        """Kicks the bomb in the direction the player is facing"""
        if not self.player.stats["ronaldinho"] or not self.can_kick:
            return

        self.obstacle_sprites.remove(self)

        # if player has ronaldinho powerup, make the bomb move at the same direction as player
        self.speed = 2

        if self.player.direction.x > 0:
            self.direction = pygame.math.Vector2(1, 0)
        elif self.player.direction.x < 0:
            self.direction = pygame.math.Vector2(-1, 0)
        elif self.player.direction.y > 0:
            self.direction = pygame.math.Vector2(0, 1)
        elif self.player.direction.y < 0:
            self.direction = pygame.math.Vector2(0, -1)

    def player_collision(self):
        """Checks collision with the player and moves the bomb"""
        player_hit = pygame.sprite.spritecollide(self, [self.player], False)

        if not player_hit:
            return

        if self.can_collide_with_player and not self.player.stats["ronaldinho"]:
            self.obstacle_sprites.add(self)

        self.kick()

    def collision(self, direction):
        """Checks for collisions with obstacles."""
        if direction == "vertical":
            objects_hit = pygame.sprite.spritecollide(
                self, self.obstacle_sprites, False
            )
            for sprite in objects_hit:
                if self.direction.y > 0:  # BAIXO
                    self.rect.bottom = sprite.rect.top
                elif self.direction.y < 0:  # CIMA
                    self.rect.top = sprite.rect.bottom

        if direction == "horizontal":
            objects_hit = pygame.sprite.spritecollide(
                self, self.obstacle_sprites, False
            )
            for sprite in objects_hit:
                if self.direction.x > 0:  # DIREITA
                    self.rect.right = sprite.rect.left
                elif self.direction.x < 0:  # ESQUERDA
                    self.rect.left = sprite.rect.right

    def move(self):
        """Moves the bomb."""
        self.rect.x += int(self.direction.x * self.speed)
        self.collision("horizontal")
        self.rect.y += int(self.direction.y * self.speed)
        self.collision("vertical")

    def update(self):
        """Updates the bomb's timer."""
        self.explosion_collision()
        self.player_collision()
        self.move()

        if self.timer > 0 and not self.player.stats["wifi_explode"]:
            self.timer -= 1
        elif self.timer <= 0 and self.is_dead is False:
            self.is_dead = True
            self.kill()
            self.explode_path(
                round_to_multiple_nearest(self.rect.y, TILE_SIZE),
                round_to_multiple_nearest(self.rect.x, TILE_SIZE),
                self.player.stats["bomb_range"],
            )
            self.player.current_bombs -= 1

        self.update_can_kick()
