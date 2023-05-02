import pygame

from player import Player


class Daniel(Player):
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

        self.name = "daniel"

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

        if keys[pygame.K_k]:
            self.spawn_bomb()

        if keys[pygame.K_l]:
            self.explode_bomb_wifi()
