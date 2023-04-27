import pygame


class Arena:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        pass
