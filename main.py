import sys
import pygame as pg

from settings import FPS, HEIGHT, WIDTH
from arena import Arena


class Game:
    """Main game class."""

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Scribbles X Sketches")

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.arena = Arena()

    def run(self):
        """Main game loop."""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill("black")
            self.arena.run()
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
