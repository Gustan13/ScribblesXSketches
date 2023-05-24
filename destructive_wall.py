from random import choice

import pygame


from tile import Tile
from powerup import PowerUp
from settings import EXPLOSION_TIME, POWERUPS_ARRAY


class DestructiveWall(Tile):
    def __init__(self, pos, groups, name, explosion_sprites, poweup_sprites):
        super().__init__(pos, groups, name)

        self.explosion_sprites = explosion_sprites
        self.powerup_sprites = poweup_sprites
        self.wall_sprites = groups[0]

        self.powerup_array = POWERUPS_ARRAY

        self.is_dead = False
        self.run_timer = True

        self.timer = EXPLOSION_TIME

    def collision_explosion(self):
        """Checks collision with explosions."""
        if self.is_dead:
            return

        explosions_hit = pygame.sprite.spritecollide(
            self, self.explosion_sprites, False
        )

        if explosions_hit:
            self.is_dead = True
            self.wall_sprites.remove(self)

    def destroy(self):
        """Destroys the wall and spawns a powerup."""
        # make this powerup spawn randomly (sometimes) based on some proportion (ronaldinho and wifi should be less common).
        PowerUp(
            (self.rect.x, self.rect.y),
            [self.powerup_sprites],
            choice(self.powerup_array),
            self.explosion_sprites,
        )
        self.run_timer = False
        self.kill()

    def spawn_powerup(self):
        """Spawns a powerup after a certain amount of time."""
        if not self.is_dead:
            return

        if not self.run_timer:
            return

        # this <= 0 prevents the destructive_wall to appear for 1 frame before the powerup.
        # Since the logic in explosion.py is self.timer > 0.
        if self.timer <= 0:
            self.destroy()
        else:
            self.timer -= 1

    def update(self):
        """Checks for collision with explosions every frame and spawns powerup if needed."""
        self.collision_explosion()
        self.spawn_powerup()
