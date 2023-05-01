import pygame

from random import choice

from tile import Tile
from powerup import PowerUp


class DestructiveWall(Tile):
    def __init__(self, pos, groups, name, explosion_sprites, poweup_sprites):
        super().__init__(pos, groups, name)

        self.explosion_sprites = explosion_sprites
        self.powerup_sprites = poweup_sprites

        self.powerup_array = [
            "max_bombs",
            "speed",
            "bomb_range",
            "ronaldinho",
            "wifi_explode",
        ]

        self.is_dead = False
        self.run_timer = True
        self.timer = 100

    def collision_explosion(self):
        if self.is_dead:
            return

        explosions_hit = pygame.sprite.spritecollide(
            self, self.explosion_sprites, False
        )

        if explosions_hit:
            self.is_dead = True

    def spawn_powerup(self):
        if not self.is_dead:
            return

        if not self.run_timer:
            return

        if self.timer < 0:
            PowerUp(
                (self.rect.x, self.rect.y),
                [self.powerup_sprites],
                choice(self.powerup_array),
                self.explosion_sprites,
            )
            self.run_timer = False
            self.kill()
        else:
            self.timer -= 1

    def update(self):
        self.collision_explosion()
        self.spawn_powerup()
