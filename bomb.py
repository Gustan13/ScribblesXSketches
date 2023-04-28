import pygame

from settings import TILE_SIZE, SPRITES_PATH


class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load(f"{SPRITES_PATH}/bomb.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)

        self.timer = 100
        self.is_dead = False

    def update(self):
        """Updates the bomb's timer."""
        if self.timer > 0:
            self.timer -= 1
        elif self.timer <= 0 and self.is_dead is False:
            self.is_dead = True
            self.kill()
