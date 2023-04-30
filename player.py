import pygame

from toolbox import floor_to_multiple
from settings import HALF_TILE, TILE_SIZE, SPRITES_PATH

from bomb import Bomb


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
    ):
        super().__init__(groups)

        self.image = pygame.image.load(f"{SPRITES_PATH}/{image_name}")
        self.image = pygame.transform.scale(self.image, (HALF_TILE, HALF_TILE))

        self.rect = self.image.get_rect(topleft=pos)

        self.rect.x += HALF_TILE // 2  # Offset
        self.rect.y += HALF_TILE // 2

        self.direction = pygame.math.Vector2()

        self.obstacle_sprites = obstacle_sprites
        self.bomb_sprites = bomb_sprites
        self.explosion_sprites = explosion_sprites

        self.bomb_delay = 0
        self.bomb_reload = 5

        self.respawn_point = self.rect.topleft

        self.stats = {  # Default stats
            "max_bombs": 2,
            "speed": 4,
            "bomb_range": 1,
            "ronaldinho": False,
            "wifi_explode": False,
        }
        self.bomb_range = 1
        self.wifi_explode_reload = 10

        self.powerup_sprites = powerup_sprites

        self.bombs_stack = []

    def spawn_bomb(self):
        """Spawns a bomb at the player's position."""
        if Bomb.num_of_bombs >= self.stats["max_bombs"]:
            return

        if self.bomb_delay > 0:
            self.bomb_delay -= 1
            return

        x_pos = floor_to_multiple(self.rect.x, TILE_SIZE)
        y_pos = floor_to_multiple(self.rect.y, TILE_SIZE)

        for bomb in self.bomb_sprites:  # Check if there's already a bomb there
            if (bomb.rect.x == x_pos) and (bomb.rect.y == y_pos):
                print("There's already a bomb there!")
                return

        # add to the stack
        self.bombs_stack.append(
            Bomb(
                (x_pos, y_pos),
                [self.bomb_sprites],
                self.obstacle_sprites,
                self.explosion_sprites,
                self,
            )
        )

        self.bomb_delay = self.bomb_reload

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

        if (
            keys[pygame.K_x]
            and self.stats["wifi_explode"]
            and self.bombs_stack
            and self.wifi_explode_reload <= 0
        ):
            self.wifi_explode_reload = 10
            self.bombs_stack[-1].timer = 0  # explode the bomb
            self.bombs_stack.pop()

    def move(self):
        """Moves the player."""
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += int(self.direction.x * self.stats["speed"])
        self.collision("horizontal")
        self.rect.y += int(self.direction.y * self.stats["speed"])
        self.collision("vertical")

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

        self.wifi_explode_reload -= 1
        self.input()
        self.move()
        self.powerup()
        self.explosions()
