import pygame

from settings import TILE_SIZE, map_2
from tile import Tile
from marcos import Marcos
from daniel import Daniel
from destructive_wall import DestructiveWall
from enum import Enum


class Tiles(Enum):
    GRASS = 0
    WALL = 1
    WALL2 = 2
    DESTRUCTIVE_WALL = 3
    MARCOS = 4
    DANIEL = 5


class Arena:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.bomb_sprites = pygame.sprite.Group()
        self.powerup_sprites = pygame.sprite.Group()
        self.explosion_sprites = pygame.sprite.Group()
        self.destructive_wall_sprites = pygame.sprite.Group()
        self.invisible_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        """Creates the map from the arrayMap in settings.py."""
        for idx_row, row in enumerate(map_2):
            for idx_col, tile in enumerate(row):
                if tile == Tiles.GRASS.value:
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )

                elif tile == Tiles.WALL.value:
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.obstacle_sprites],
                        "wall.png",
                    )

                elif tile == Tiles.WALL2.value:
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.obstacle_sprites],
                        "wall2.png",
                    )

                elif tile == Tiles.DESTRUCTIVE_WALL.value:
                    DestructiveWall(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.destructive_wall_sprites, self.invisible_sprites],
                        "destructive_wall.png",
                        self.explosion_sprites,
                        self.powerup_sprites,
                    )
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )

                elif tile == Tiles.MARCOS.value:
                    Marcos(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.player_sprite],
                        "marcos1.png",
                        self.obstacle_sprites,
                        self.bomb_sprites,
                        self.powerup_sprites,
                        self.explosion_sprites,
                        self.destructive_wall_sprites,
                        "marcos",
                    )
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )
                elif tile == Tiles.DANIEL.value:
                    Daniel(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.player_sprite],
                        "daniel1.png",
                        self.obstacle_sprites,
                        self.bomb_sprites,
                        self.powerup_sprites,
                        self.explosion_sprites,
                        self.destructive_wall_sprites,
                        "daniel",
                    )
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )

    def run(self):
        """Main arena loop."""
        self.visible_sprites.draw(self.display_surface)

        self.destructive_wall_sprites.draw(self.display_surface)

        self.bomb_sprites.draw(self.display_surface)
        self.player_sprite.draw(self.display_surface)
        self.powerup_sprites.draw(self.display_surface)

        self.explosion_sprites.draw(self.display_surface)

        self.obstacle_sprites.draw(self.display_surface)

        self.player_sprite.update()
        self.bomb_sprites.update()
        self.powerup_sprites.update()
        self.obstacle_sprites.update()
        self.invisible_sprites.update()
        self.explosion_sprites.update()
        self.destructive_wall_sprites.update()
