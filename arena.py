import pygame

from random import choice

from settings import TILE_SIZE, arrayMap
from tile import Tile
from powerup import PowerUp
from player import Player


class Arena:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.bomb_sprites = pygame.sprite.Group()
        self.powerup_sprites = pygame.sprite.Group()
        self.explosion_sprites = pygame.sprite.Group()

        self.powerup_array = [
            "max_bombs",
            "speed",
            "bomb_range",
            "ronaldinho",
            "wifi_explode",
        ]

        self.create_map()

    def create_map(self):
        """Creates the map from the arrayMap in settings.py."""
        for idx_row, row in enumerate(arrayMap):
            for idx_col, col in enumerate(row):
                if col == 1:
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.obstacle_sprites],
                        "test.png",
                    )
                elif col == 0:
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )
                elif col == 2:
                    Player(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.player_sprite],
                        "marcos.png",
                        self.obstacle_sprites,
                        self.bomb_sprites,
                        self.powerup_sprites,
                        self.explosion_sprites,
                    )
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )
                elif col == 3:
                    PowerUp(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.powerup_sprites],
                        # select random powerup
                        choice(self.powerup_array),
                        self.explosion_sprites,
                    )
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )

    def run(self):
        """Main arena loop."""
        self.visible_sprites.draw(self.display_surface)

        self.bomb_sprites.draw(self.display_surface)
        self.player_sprite.draw(self.display_surface)
        self.powerup_sprites.draw(self.display_surface)

        self.explosion_sprites.draw(self.display_surface)

        self.obstacle_sprites.draw(self.display_surface)

        self.player_sprite.update()
        self.bomb_sprites.update()
        self.powerup_sprites.update()
        self.obstacle_sprites.update()
        self.explosion_sprites.update()
