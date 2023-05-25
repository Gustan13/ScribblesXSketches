import pygame
from tile import Tile


class PowerUp(Tile):
    def __init__(self, pos, groups, powerup_type, explosion_sprites):
        super().__init__(pos, groups, f"powerups/{powerup_type}.png")
        self.powerup_type = powerup_type
        self.explosion_sprites = explosion_sprites

        self.sound = pygame.mixer.Sound("sounds/Item Get.wav")

    def speed_up(self, stats):
        """Increases the player's speed by 1."""
        stats["speed"] += 1

        # play some particle animation here maybe

    def increase_max_bombs(self, stats):
        """Increases the player's max bombs by 1."""
        stats["max_bombs"] += 1

    def increase_range_of_bombs(self, stats):
        """Increases the player's bomb range by 1."""
        stats["bomb_range"] += 1

    def kick_bombs(self, stats):
        """Allows the player to kick bombs."""
        stats["ronaldinho"] = True

    def wifi_explode(self, stats):
        """Allows the player to explode bombs remotely."""
        stats["wifi_explode"] = True

    def apply(self, stats):
        """Applies the powerup to the player."""

        self.play_sound()
        if self.powerup_type == "speed":
            self.speed_up(stats)
        elif self.powerup_type == "max_bombs":
            self.increase_max_bombs(stats)
        elif self.powerup_type == "bomb_range":
            self.increase_range_of_bombs(stats)
        elif self.powerup_type == "ronaldinho":
            self.kick_bombs(stats)
        elif self.powerup_type == "wifi_explode":
            self.wifi_explode(stats)

    def explosion_collision(self):
        """Checks collision with explosions"""
        explosions_hit = pygame.sprite.spritecollide(
            self, self.explosion_sprites, False
        )

        if explosions_hit:
            self.kill()

    def play_sound(self):
        """Plays the powerup sound."""
        self.sound.play()

    def update(self):
        """Checks for collision with explosions every frame."""
        self.explosion_collision()
