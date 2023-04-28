from typing import Tuple
import pygame


class Tile(pygame.sprite.Sprite):
    """A tile object that can be placed on the screen."""

    def __init__(
        self,
        pos: Tuple[int, int],
        groups: list[pygame.sprite.Group],
        name: str,
    ):
        super().__init__(groups)  # type: ignore

        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect(topleft=pos)
