import pygame

from settings import TILE_SIZE, arrayMap
from tile import Tile


class Arena:
    """The arena object that contains the map and all the sprites."""

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        """Create the map from the arrayMap in settings.py."""
        for row, row_list in enumerate(arrayMap):
            for col, tile in enumerate(row_list):
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
        """Draw the arena."""
        self.obstacle_sprites.draw(self.display_surface)
