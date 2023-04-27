import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.rect = pygame.rect.Rect(250, 250, 50, 50)
