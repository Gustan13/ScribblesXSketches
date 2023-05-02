import pygame

from player import Player


class Marcos(Player):
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
    ):
        super().__init__(
            pos,
            groups,
            image_name,
            obstacle_sprites,
            bomb_sprites,
            powerup_sprites,
            explosion_sprites,
            destructive_wall_sprites,
            "marcos",
        )

        self.name = "marcos"

    def input(self):
        """Handles player input."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_c]:
            self.spawn_bomb()

        if keys[pygame.K_v]:
            self.explode_bomb_wifi()
