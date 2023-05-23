import pygame
from player import Player


class Daniel(Player):
    # only override input
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

        if keys[pygame.K_n]:
            self.spawn_bomb()

        if keys[pygame.K_m]:
            self.explode_bomb_wifi()
