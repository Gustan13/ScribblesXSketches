import pygame

from settings import *
from tile import Tile


class Arena:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row, list in enumerate(arrayMap):
            for col, tile in enumerate(list):
                if tile == 1:
                    Tile(
                        (col * TILE_SIZE, row * TILE_SIZE),
                        [self.obstacle_sprites],
                        "test.png",
                    )
                else:
                    Tile(
                        (col * TILE_SIZE, row * TILE_SIZE),
                        [self.obstacle_sprites],
                        "grass.png",
                    )

    def run(self):
        self.obstacle_sprites.draw(self.display_surface)
