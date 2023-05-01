import pathlib
import pygame


from settings import TILE_SIZE, SPRITES_PATH


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, name):
        super().__init__(groups)

        self.image = pygame.image.load(pathlib.Path(SPRITES_PATH, name))
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)
