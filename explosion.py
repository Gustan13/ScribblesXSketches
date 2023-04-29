import pygame

from settings import *


class Explosion(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load(f"{SPRITES_PATH}/marcos.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)

        self.timer = 100

    def destroy(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.kill()

    def update(self):
        self.destroy()