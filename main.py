import sys
import pygame as pg

from settings import FPS, HEIGHT, WIDTH
from arena import Arena
from mainmenu import MainMenu


class Game:
    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Scribbles vs. Sketches")

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        mainmenu = MainMenu(self.screen, self.clock)

        mainmenu.draw()
        mainmenu.play()

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
