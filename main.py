import pygame as pg
import sys

from settings import *


class Game:
    def __init__(self) -> None:
        pg.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Scribbles X Sketches")
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill("blue")
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
