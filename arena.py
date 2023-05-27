import random
import pygame

from settings import TILE_SIZE, HEIGHT, WIDTH, map_4
from tile import Tile
from marcos import Marcos
from daniel import Daniel
from destructive_wall import DestructiveWall
from enum import Enum

font = pygame.font.Font("./font/Minecraft.ttf", 20)

class Tiles(Enum):
    GRASS = 0
    WALL = 1
    WALL2 = 2
    DESTRUCTIVE_WALL = 3
    MARCOS = 4
    DANIEL = 5


class Arena:
    def __init__(self, max_score):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.bomb_sprites = pygame.sprite.Group()
        self.powerup_sprites = pygame.sprite.Group()
        self.explosion_sprites = pygame.sprite.Group()
        self.destructive_wall_sprites = pygame.sprite.Group()
        self.invisible_sprites = pygame.sprite.Group()

        self.marcos_image = pygame.image.load("sprites/marcos1.png")
        self.marcos_image = pygame.transform.scale(self.marcos_image, (TILE_SIZE, TILE_SIZE))
        self.daniel_image = pygame.image.load("sprites/daniel1.png")
        self.daniel_image = pygame.transform.scale(self.daniel_image, (TILE_SIZE, TILE_SIZE))

        self.player_killed = False

        self.create_map()

        self.marcos_score = 0
        self.daniel_score = 0

        self.max_points = max_score

    def update_hud(self):
        marcos_text = font.render("Marcos", True, "black")
        daniel_text = font.render("Daniel", True, "black")

        self.display_surface.blit(
            marcos_text,
            (5, HEIGHT - (TILE_SIZE - 10)),
        )
        self.display_surface.blit(
            daniel_text,
            (WIDTH/2, HEIGHT - (TILE_SIZE - 10)),
        )

        for score in range(self.marcos_score):
            self.display_surface.blit(self.marcos_image, (75 + score * TILE_SIZE, HEIGHT - TILE_SIZE))
        for score in range(self.daniel_score):
            self.display_surface.blit(self.daniel_image, (score * TILE_SIZE + 75 + WIDTH/2, HEIGHT - TILE_SIZE))

    def reset_arena(self):
        self.visible_sprites.empty()
        self.obstacle_sprites.empty()
        self.bomb_sprites.empty()
        self.powerup_sprites.empty()
        self.explosion_sprites.empty()
        self.destructive_wall_sprites.empty()
        self.invisible_sprites.empty()

        for player in self.player_sprite.sprites():
            player.is_dead = False
            player.respawn()

        self.player_killed = True

        self.create_map()

    def create_map(self):
        """Creates the map from the arrayMap in settings.py."""
        for idx_row, row in enumerate(map_4):
            for idx_col, tile in enumerate(row):
                random_grass = random.choice(["grass.png", "grass1.png"])

                if tile == Tiles.GRASS.value:
                    Tile(
                        (idx_col * TILE_SIZE, idx_row * TILE_SIZE),
                        [self.visible_sprites],
                        random_grass,
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
                    if self.player_killed == False:
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
                    if self.player_killed == False:
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

        self.update_hud()

        for player in self.player_sprite.sprites():
            if not player.is_dead:
                continue

            if player.name == "marcos":
                self.daniel_score += 1

            elif player.name == "daniel":
                self.marcos_score += 1

            if self.marcos_score == self.max_points:
                celebration("marcos")
            elif self.daniel_score == self.max_points:
                celebration("daniel")

            print("Marcos:", self.marcos_score, "Daniel:", self.daniel_score)

            self.update_hud()
            self.reset_arena()
            break