import pygame

from settings import *
from tile import Tile
from player import Player


class Arena:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.bomb_sprites = pygame.sprite.Group()

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
                elif tile == 0:
                    Tile(
                        (col * TILE_SIZE, row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )
                elif tile == 2:
                    Player(
                        (col * TILE_SIZE, row * TILE_SIZE),
                        [self.player_sprite],
                        "marcos.png",
                        self.obstacle_sprites,
                        self.bomb_sprites,
                    )
                    Tile(
                        (col * TILE_SIZE, row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )

    def run(self):
        self.obstacle_sprites.draw(self.display_surface)
        self.visible_sprites.draw(self.display_surface)

        self.bomb_sprites.draw(self.display_surface)
        self.player_sprite.draw(self.display_surface)

        self.player_sprite.update()
        self.bomb_sprites.update()
