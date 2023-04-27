import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, name):
        super().__init__(groups)

        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect(topleft=pos)
