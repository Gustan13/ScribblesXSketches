import pygame

from tile import Tile
from explosion import Explosion

from settings import TILE_SIZE, FPS
from toolbox import check_group_positions, round_to_nearest


class Bomb(Tile):
    def __init__(
        self,
        pos,
        groups,
        obstacle_sprites,
        explosion_sprites,
        destructive_wall_sprites,
        player_group,
        player_sprite_owner,
    ):
        super().__init__(pos, groups, "bomb.png")

        self.timer = FPS * 4.5  # 4.5 seconds
        self.is_dead = False

        self.player_group = player_group[0]
        self.player = player_sprite_owner

        self.obstacle_sprites = obstacle_sprites
        self.explosion_sprites = explosion_sprites
        self.destructive_wall_sprites = destructive_wall_sprites

        self.bomb_sprite_group = groups[0]

        self.can_collide_with_player = False

        self.is_bomb = True

        self.speed = 2
        self.direction = pygame.math.Vector2(0, 0)

    def collision(self, direction, obstacles):
        """Checks for collisions with obstacles."""
        if direction == "vertical":
            objects_hit = pygame.sprite.spritecollide(self, obstacles, False)
            for sprite in objects_hit:
                if sprite == self:
                    continue

                if self.direction.y > 0:  # BAIXO
                    self.rect.bottom = sprite.rect.top
                elif self.direction.y < 0:  # CIMA
                    self.rect.top = sprite.rect.bottom

        if direction == "horizontal":
            objects_hit = pygame.sprite.spritecollide(self, obstacles, False)
            for sprite in objects_hit:
                if sprite == self:
                    continue

                if self.direction.x > 0:  # DIREITA
                    self.rect.right = sprite.rect.left
                elif self.direction.x < 0:  # ESQUERDA
                    self.rect.left = sprite.rect.right

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
            if check_group_positions(
                (col + TILE_SIZE * aux, row), self.destructive_wall_sprites
            ):
                break
            aux += 1

        aux = 1

        # explode to the left
        while (
            not check_group_positions(
                (col - TILE_SIZE * aux, row), self.obstacle_sprites
            )
        ) and (aux <= size):
            Explosion((col - TILE_SIZE * aux, row), [self.explosion_sprites])
            if check_group_positions(
                (col - TILE_SIZE * aux, row), self.destructive_wall_sprites
            ):
                break
            aux += 1

        aux = 1

        # explode down
        while (
            not check_group_positions(
                (col, row + TILE_SIZE * aux), self.obstacle_sprites
            )
        ) and (aux <= size):
            Explosion((col, row + TILE_SIZE * aux), [self.explosion_sprites])
            if check_group_positions(
                (col, row + TILE_SIZE * aux), self.destructive_wall_sprites
            ):
                break
            aux += 1

        aux = 1

        # explode up
        while (
            not check_group_positions(
                (col, row - TILE_SIZE * aux), self.obstacle_sprites
            )
        ) and (aux <= size):
            Explosion((col, row - TILE_SIZE * aux), [self.explosion_sprites])
            if check_group_positions(
                (col, row - TILE_SIZE * aux), self.destructive_wall_sprites
            ):
                break
            aux += 1

        return

    def explosion_collision(self):
        """Checks collision with explosions"""
        explosions_hit = pygame.sprite.spritecollide(
            self, self.explosion_sprites, False
        )

        if explosions_hit:
            self.explode()

    def collide_bomb_with_bomb(self):
        """Checks collision with other bombs"""
        pass
        # bombs_hit = pygame.sprite.spritecollide(
        #     self, self.bomb_sprite_group, False, pygame.sprite.collide_rect_ratio(1.00)
        # )

        # for bomb in bombs_hit:
        #     if bomb == self:
        #         continue

        #     if bomb.speed > 0:
        #         print("switch")
        #         bomb.speed, self.speed = self.speed, bomb.speed
        #         bomb.direction, self.direction = self.direction, bomb.direction

        #         bomb.rect.x = round_to_nearest(bomb.rect.x, TILE_SIZE)
        #         bomb.rect.y = round_to_nearest(bomb.rect.y, TILE_SIZE)

    def collide_with_player(self):
        """Checks collision with player"""
        if self.can_collide_with_player:
            return

        player_hit = pygame.sprite.spritecollide(
            self, self.player_group, False, pygame.sprite.collide_rect_ratio(1.2)
        )

        if not player_hit:
            self.obstacle_sprites.add(self)
            self.can_collide_with_player = True

    def is_player_colliding_with_bomb(self):
        """Checks if player is colliding with bomb"""
        if not self.can_collide_with_player:
            return False

        player_hit = pygame.sprite.spritecollide(
            self, self.player_group, False, pygame.sprite.collide_rect_ratio(1.2)
        )

        return player_hit

    def calculate_edge_collision(self):
        """Calculates the edges of the bomb and player"""
        left_edge = pygame.Rect(
            self.rect.topleft[0] - 1, self.rect.topleft[1], 1, TILE_SIZE
        )
        top_edge = pygame.Rect(
            self.rect.topleft[0], self.rect.topleft[1] - 1, TILE_SIZE, 1
        )
        right_edge = pygame.Rect(*self.rect.topright, 1, TILE_SIZE)
        bottom_edge = pygame.Rect(*self.rect.bottomleft, TILE_SIZE, 1)

        return (
            # add the two player rects to the tuple
            left_edge.collidelist(self.player_group.sprites()),
            top_edge.collidelist(self.player_group.sprites()),
            right_edge.collidelist(self.player_group.sprites()),
            bottom_edge.collidelist(self.player_group.sprites()),
        )

    def kick(self, player):
        """Kicks the bomb in the direction the player is facing"""
        if not player:
            return

        if len(player) >= 2:
            print("More than one player collided with bomb")
            self.explode()
            return

        # player = player[0]

        if self.player.stats["ronaldinho"] is False:
            return False

        # if player has ronaldinho powerup, make the bomb move at the same direction as player

        self.speed = 4

        left, top, right, bottom = self.calculate_edge_collision()

        if left != -1:
            self.direction = pygame.math.Vector2(1, 0)
        elif right != -1:
            self.direction = pygame.math.Vector2(-1, 0)
        if top != -1:
            self.direction = pygame.math.Vector2(0, 1)
        elif bottom != -1:
            self.direction = pygame.math.Vector2(0, -1)

    def move(self):
        """Moves the bomb."""
        self.rect.x += int(self.direction.x * self.speed)
        self.collision("horizontal", self.obstacle_sprites)
        self.collision("horizontal", self.destructive_wall_sprites)
        self.rect.y += int(self.direction.y * self.speed)
        self.collision("vertical", self.obstacle_sprites)
        self.collision("vertical", self.destructive_wall_sprites)

    def explode(self):
        """Explodes the bomb setting the timer to 0."""
        self.timer = 0

    def update(self):
        """Updates the bomb's timer."""
        self.explosion_collision()
        self.collide_with_player()
        self.collide_bomb_with_bomb()

        s = self.is_player_colliding_with_bomb()

        if s:
            self.kick(s)

        if self.timer > 0 and self.player.stats["wifi_explode"] is False:
            self.timer -= 1
        elif self.timer <= 0 and self.is_dead is False:
            self.is_dead = True
            self.kill()
            self.explode_path(
                round_to_nearest(self.rect.y, TILE_SIZE),
                round_to_nearest(self.rect.x, TILE_SIZE),
                self.player.stats["bomb_range"],
            )
            self.player.current_bombs -= 1

        if self.speed > 0:
            self.move()
