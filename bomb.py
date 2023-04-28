import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("bomb.png")
        self.rect = self.image.get_rect(topleft=pos)

        self.timer = 60
        self.isDead = False

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        elif self.timer <= 0 and self.isDead == False:
            self.isDead = True
            self.kill()
