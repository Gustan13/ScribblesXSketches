import pathlib
import pygame

from toolbox import floor_to_multiple
from settings import FPS, HALF_TILE, TILE_SIZE, SPRITES_PATH, DEFAULT_POWERUP_STATS

from bomb import Bomb
from animation import Animation


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        pos,
        groups,
        image_name,
        obstacle_sprites,
        bomb_sprites,
        powerup_sprites,
        explosion_sprites,
        destructive_wall_sprites,
        name,
    ):
        super().__init__(groups)

        self.player_group = groups

        self.image = pygame.image.load(pathlib.Path(SPRITES_PATH, image_name))
        self.image = pygame.transform.scale(self.image, (HALF_TILE, HALF_TILE))

        self.rect = self.image.get_rect(topleft=pos)

        self.rect.x += HALF_TILE // 2  # Offset
        self.rect.y += HALF_TILE // 2

        self.direction = pygame.math.Vector2()

        self.obstacle_sprites = obstacle_sprites
        self.bomb_sprites = bomb_sprites
        self.explosion_sprites = explosion_sprites
        self.destructive_wall_sprites = destructive_wall_sprites

        self.bomb_delay = 0
        self.bomb_reload = 5

        self.respawn_point = self.rect.topleft

        self.stats = DEFAULT_POWERUP_STATS.copy()

        self.powerup_sprites = powerup_sprites

        self.current_bombs = 0

        self.wifi_timer = FPS / 4  # 1/4 of frame (15ms in 60fps)

        self.idle_animation = Animation(name, 2, 5, HALF_TILE)
        self.walk_animation = Animation(name + "_walk_", 3, 5, HALF_TILE)

    def explode_bomb_wifi(self):
        """Explodes the player's bombs."""
        if self.stats["wifi_explode"] is False:
            return

        if self.current_bombs == 0 or self.wifi_timer > 0:
            return

        self.wifi_timer = FPS / 4  # reset the timer

        # get bombs from the player
        for bomb in self.bomb_sprites:
            if bomb.player == self:
                bomb.explode()
                break

    def update_wifi_timer(self):
        """Updates the wifi timer."""
        if self.stats["wifi_explode"] is False:
            return

        if self.wifi_timer > 0:
            self.wifi_timer -= 1

    def spawn_bomb(self):
        """Spawns a bomb at the player's position."""
        if self.current_bombs >= self.stats["max_bombs"]:
            return

        if self.current_bombs == 1:  # first bomb has no cooldown
            self.bomb_delay = 0

        if self.bomb_delay > 0:
            self.bomb_delay -= 1
            return

        x_pos = floor_to_multiple(self.rect.x, TILE_SIZE)
        y_pos = floor_to_multiple(self.rect.y, TILE_SIZE)

        for bomb in self.bomb_sprites:  # Check if there's already a bomb there
            if (bomb.rect.x == x_pos) and (bomb.rect.y == y_pos):
                return

        # if already a player in the position, don't spawn a bomb
        for player in self.player_group[0]:
            if player == self:
                continue
            if (floor_to_multiple(player.rect.x, TILE_SIZE) == x_pos) and (floor_to_multiple(player.rect.y, TILE_SIZE) == y_pos):
                return
        Bomb(
            (x_pos, y_pos),
            [self.bomb_sprites],
            self.obstacle_sprites,
            self.explosion_sprites,
            self.destructive_wall_sprites,
            self.player_group,
            self,
        )

        self.bomb_delay = self.bomb_reload

        self.current_bombs += 1

    def input(self):
        """Handles player input."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_z]:
            self.spawn_bomb()

        if keys[pygame.K_x]:
            self.explode_bomb_wifi()

    def move(self):
        """Moves the player."""

        if self.direction.x == 1:
            self.walk_animation.mirrored = False
            self.walk_animation.play(self)
        elif self.direction.x == -1:
            self.walk_animation.mirrored = True
            self.walk_animation.play(self)
        elif self.direction.y == -1 or self.direction.y == 1:
            self.walk_animation.play(self)
        else:
            self.idle_animation.mirrored = self.walk_animation.mirrored
            self.idle_animation.play(self)

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += int(self.direction.x * self.stats["speed"])
        self.collision("horizontal", self.obstacle_sprites)
        self.collision("horizontal", self.destructive_wall_sprites)
        self.rect.y += int(self.direction.y * self.stats["speed"])
        self.collision("vertical", self.obstacle_sprites)
        self.collision("vertical", self.destructive_wall_sprites)

    def collision(self, direction, obstacles):
        """Checks for collisions with obstacles."""
        if direction == "vertical":
            objects_hit = pygame.sprite.spritecollide(self, obstacles, False)
            for sprite in objects_hit:
                if self.direction.y > 0:  # BAIXO
                    self.rect.bottom = sprite.rect.top
                elif self.direction.y < 0:  # CIMA
                    self.rect.top = sprite.rect.bottom

        if direction == "horizontal":
            objects_hit = pygame.sprite.spritecollide(self, obstacles, False)
            for sprite in objects_hit:
                if self.direction.x > 0:  # DIREITA
                    self.rect.right = sprite.rect.left
                elif self.direction.x < 0:  # ESQUERDA
                    self.rect.left = sprite.rect.right

    def powerup(self):
        """Checks for collisions with powerups."""
        objects_hit = pygame.sprite.spritecollide(self, self.powerup_sprites, True)

        for sprite in objects_hit:
            sprite.apply(self.stats)
            sprite.kill()

            print(self.stats)

    def explosions(self):
        """Checks for collisions with explosions and respawns player"""
        explosions_hit = pygame.sprite.spritecollide(
            self, self.explosion_sprites, False
        )

        if explosions_hit:
            self.rect.topleft = self.respawn_point

    def update(self):
        """Main player loop that runs every frame."""
        self.input()
        self.move()
        self.powerup()
        self.explosions()
        self.update_wifi_timer()
