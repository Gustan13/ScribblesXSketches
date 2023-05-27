import math
import pygame
from settings import WIDTH, HEIGHT, TILE_SIZE

pygame.font.init()

font = pygame.font.Font("./font/Minecraft.ttf", 36)
big_font = pygame.font.Font("./font/Minecraft.ttf", 60)


def calculate_centered_position(text: str, x: int, y: int):
    """Calculates the centered position of a text"""
    text_width, text_height = font.size(text)
    return (x - text_width // 2, y - text_height // 2)


def calculate_centered_position_big(text: str, x: int, y: int):
    """Calculates the centered position of a text in big font"""
    text_width, text_height = big_font.size(text)
    return (x - text_width // 2, y - text_height // 2)


class MainMenu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.is_running = True
        self.is_start_game_selected = True

        self.music = pygame.mixer.Sound("sounds/intro.mp3")
        self.music.play()

        self.sounds = {
            "move": pygame.mixer.Sound("./sounds/move cursor.mp3"),
            "select": pygame.mixer.Sound("./sounds/Select.wav"),
        }

        self.controls_image = pygame.image.load("images/controls.png")
        self.controls_image = pygame.transform.scale(
            self.controls_image, (WIDTH, HEIGHT)
        )

        self.title_opacity = 0
        self.foreground_image = pygame.image.load("images/textinho.png")
        self.foreground_image = pygame.transform.scale(
            self.foreground_image, (WIDTH, HEIGHT)
        )
        self.show_controls = False
        self.background_image = pygame.image.load("images/background.png")
        self.background_image = pygame.transform.scale(
            self.background_image, (WIDTH, HEIGHT)
        )
        clock.tick(10)  # 10 FPS

    def draw(self):
        """Draws the main menu"""
        text_3 = "Scribbles vs. Sketches"
        text_1 = "Start Game"
        text_2 = "Controls"
        # make the background an image
        if self.title_opacity < 255:
            self.title_opacity += 2

        self.screen.blit(self.background_image, (0, 0))

        self.foreground_image.set_alpha(min(255, self.title_opacity * 2))
        self.screen.blit(self.foreground_image, (0, 0))

        self.screen.blit(
            self.foreground_image,
            (0, 0),
        )

        big_font_surface = big_font.render(text_3, True, "black")
        big_font_surface.set_alpha(min(255, self.title_opacity * 2))
        self.screen.blit(
            big_font_surface,
            calculate_centered_position_big(text_3, WIDTH // 2, 128),
        )

        if self.is_start_game_selected:
            font_surf = font.render(f"> {text_1}", True, "white")
            font_surf.set_alpha(self.title_opacity)
            self.screen.blit(
                font_surf,
                calculate_centered_position(
                    text_1, WIDTH // 2, HEIGHT // 2 - TILE_SIZE
                ),
            )

            font_surf = font.render(text_2, True, "white")
            font_surf.set_alpha(self.title_opacity)

            self.screen.blit(
                font_surf,
                calculate_centered_position(
                    text_2, WIDTH // 2, HEIGHT // 2 + TILE_SIZE
                ),
            )
        else:
            font_surf = font.render(text_1, True, "white")
            font_surf.set_alpha(self.title_opacity)
            self.screen.blit(
                font_surf,
                calculate_centered_position(
                    text_1, WIDTH // 2, HEIGHT // 2 - TILE_SIZE
                ),
            )

            font_surf = font.render(f"> {text_2}", True, "white")
            font_surf.set_alpha(self.title_opacity)
            self.screen.blit(
                font_surf,
                calculate_centered_position(
                    text_2, WIDTH // 2, HEIGHT // 2 + TILE_SIZE
                ),
            )

    def draw_controls(self):
        """Draws the controls screen"""
        self.screen.blit(self.controls_image, (0, 0))

        text_1 = "Press Esc to go back"
        text_2 = "Marcos"
        text_3 = "Daniel"

        self.screen.blit(
            font.render(text_1, True, "white"),
            calculate_centered_position(text_1, WIDTH // 2, HEIGHT - 50),
        )

        self.screen.blit(
            font.render(text_2, True, (255, 60, 48)),
            calculate_centered_position(text_2, WIDTH // 2, HEIGHT // 5 - 30),
        )

        self.screen.blit(
            font.render(text_3, True, (0, 187, 220)),
            calculate_centered_position(text_3, WIDTH // 2, HEIGHT // 1.5),
        )

    def play(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if not self.show_controls:
                            self.sounds["select"].play()
                        if self.is_start_game_selected:
                            self.is_running = False
                            self.music.stop()
                        else:
                            self.show_controls = True
                    if event.key == pygame.K_ESCAPE:
                        self.sounds["select"].play()
                        self.show_controls = False
                    if event.key == pygame.K_UP:
                        if not self.is_start_game_selected:
                            self.sounds["move"].play()
                        self.is_start_game_selected = True
                    if event.key == pygame.K_DOWN:
                        if self.is_start_game_selected:
                            self.sounds["move"].play()
                        self.is_start_game_selected = False

            if self.show_controls:
                self.draw_controls()
            else:
                self.draw()

            pygame.display.update()  # update the display
