import pygame

from settings import *


class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("bomb.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)

        self.timer = 100
        self.isDead = False

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        elif self.timer <= 0 and self.isDead == False:
            self.isDead = True
            self.kill()
