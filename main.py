import sys
import pygame as pg
from pause import Pause

from settings import FPS, HEIGHT, WIDTH
from arena import Arena
from mainmenu import MainMenu

from cutscene import cutscene1, cutscene2, cutscene3


class Game:
    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Scribbles vs. Sketches")

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.mainmenu = MainMenu(self.screen, self.clock)

        self.mainmenu.draw()
        self.mainmenu.play()

        self.cutscene1 = cutscene1()
        self.cutscene2 = cutscene2()
        self.cutscene3 = cutscene3()

        self.cutscene1.play()
        self.cutscene2.play()
        self.cutscene3.play()

        self.game_type = 3

        self.arena = Arena(self.game_type)
        self.is_paused = False
        self.pause_menu = Pause(self.screen)

    def return_menu(self):
        self.mainmenu = MainMenu(self.screen, self.clock)
        self.arena = Arena(self.game_type)
        self.is_paused = False
        self.mainmenu.draw()
        self.mainmenu.play()

    def draw_pause(self):
        """Pause the game."""
        self.pause_menu.draw()

        res = self.pause_menu.update()

        if res == "quit":
            pg.quit()
            sys.exit()
        elif res == "resume":
            self.is_paused = False
        elif res == "main_menu":
            self.return_menu()

        elif res == "options":
            print("options")  # TODO: Make this a trolling

    def run(self):
        """Main game loop."""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE or event.key == pg.K_p:
                        self.is_paused = not self.is_paused

            pg.display.update()

            if self.is_paused:
                self.draw_pause()
                continue

            self.screen.fill("black")
            if self.arena.game_end:
                self.return_menu()
            else:
                self.arena.run()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
