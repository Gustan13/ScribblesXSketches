import pygame
from tile import Tile
from settings import EXPLOSION_TIME, TILE_SIZE, TILES_PATH


class Explosion(Tile):
    def __init__(self, pos, groups):
        super().__init__(pos, groups, "explosion_center.png")

        self.image_horizontal = pygame.image.load(f"{TILES_PATH}/explosion_path.png")
        self.image_horizontal = pygame.transform.scale(
            self.image_horizontal, (TILE_SIZE, TILE_SIZE)
        )

        self.image_corner = pygame.image.load(f"{TILES_PATH}/explosion_edge.png")
        self.image_corner = pygame.transform.scale(
            self.image_corner, (TILE_SIZE, TILE_SIZE)
        )

        self.image_center = pygame.image.load(f"{TILES_PATH}/explosion_center.png")
        self.image_center = pygame.transform.scale(
            self.image_center, (TILE_SIZE, TILE_SIZE)
        )

        self.images_list = {
            "center": self.image_center,
            "horizontal": self.image_horizontal,
            "vertical": pygame.transform.rotate(self.image_horizontal, 90),
            "corner_left": self.image_corner,
            "corner_right": pygame.transform.flip(self.image_corner, True, False),
            "corner_down": pygame.transform.rotate(self.image_corner, 90),
            "corner_up": pygame.transform.rotate(self.image_corner, 270),
        }

        self.timer = EXPLOSION_TIME

    def destroy(self):
        """Destroys the explosion after a certain amount of time."""
        if self.timer > 0:
            self.timer -= 1
        else:
            self.kill()

    def update(self):
        """Updates the explosion."""
        self.destroy()
