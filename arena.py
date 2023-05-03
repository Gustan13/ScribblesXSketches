import pygame

from settings import TILE_SIZE, arrayMap
from tile import Tile
from marcos import Marcos
from daniel import Daniel
from destructive_wall import DestructiveWall
from powerup import PowerUp


class Arena:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()

        self.invisible_sprites = (
            pygame.sprite.Group()
        )  # invisible sprites are not drawn but still updated

        self.obstacle_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.bomb_sprites = pygame.sprite.Group()
        self.powerup_sprites = pygame.sprite.Group()
        self.explosion_sprites = pygame.sprite.Group()
        self.destructive_wall_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        """Creates the map from the arrayMap in settings.py."""
        for idx_row, row in enumerate(arrayMap):
            for idx_col, tile in enumerate(row):
                if tile == 0:
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )
                elif tile == 1:
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.obstacle_sprites],
                        "test.png",
                    )
                elif tile == 2:
                    Marcos(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.player_sprite],
                        "marcos1.png",
                        self.obstacle_sprites,
                        self.bomb_sprites,
                        self.powerup_sprites,
                        self.explosion_sprites,
                        self.destructive_wall_sprites,
                    )
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )
                elif tile == 3:
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
                elif tile == 4:
                    Daniel(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.player_sprite],
                        "marcos1.png",
                        self.obstacle_sprites,
                        self.bomb_sprites,
                        self.powerup_sprites,
                        self.explosion_sprites,
                        self.destructive_wall_sprites,
                    )
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        "grass.png",
                    )
                elif tile == 5:
                    PowerUp(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.powerup_sprites],
                        "ronaldinho",
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
