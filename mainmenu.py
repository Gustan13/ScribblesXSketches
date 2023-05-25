import pygame
from settings import WIDTH, HEIGHT, FPS, TILE_SIZE

pygame.font.init()

font = pygame.font.Font("./font/Minecraft.ttf", 36)


def calculate_centered_position(text: str, x: int, y: int):
    text_width, text_height = font.size(text)
    return (x - text_width // 2, y - text_height // 2)


class MainMenu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.is_running = True
        self.is_start_game_selected = True

        self.sounds = {
            "move": pygame.mixer.Sound("./sounds/Select.wav"),
            "select": pygame.mixer.Sound("./sounds/Pause.wav"),
        }

        self.controls_image = pygame.image.load("images/controls.png")
        self.controls_image = pygame.transform.scale(
            self.controls_image, (WIDTH, HEIGHT)
        )

        self.show_controls = False
        clock.tick(5)

    def draw(self):
        text_1 = "Scribbles vs. Sketches"
        text_2 = "Start Game"
        text_3 = "Controls"
        # make the background an image
        background_image = pygame.image.load("images/background.png")
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        self.screen.blit(background_image, (0, 0))

        if self.is_start_game_selected:
            self.screen.blit(
                font.render(f"> {text_2}", True, "white"),
                calculate_centered_position(
                    text_2, WIDTH // 2, HEIGHT // 2 - TILE_SIZE
                ),
            )
            self.screen.blit(
                font.render(text_3, True, "white"),
                calculate_centered_position(
                    text_3, WIDTH // 2, HEIGHT // 2 + TILE_SIZE
                ),
            )
        else:
            self.screen.blit(
                font.render(text_2, True, "white"),
                calculate_centered_position(
                    text_2, WIDTH // 2, HEIGHT // 2 - TILE_SIZE
                ),
            )
            self.screen.blit(
                font.render(f"> {text_3}", True, "white"),
                calculate_centered_position(
                    text_3, WIDTH // 2, HEIGHT // 2 + TILE_SIZE
                ),
            )

    def draw_controls(self):
        self.screen.blit(self.controls_image, (0, 0))

        text_1 = "Press Esc to go back"
        text_2 = "Marcos"
        text_3 = "Daniel"

        self.screen.blit(
            font.render(text_1, True, "white"),
            calculate_centered_position(text_1, WIDTH // 2, HEIGHT - 50),
        )

        self.screen.blit(
            font.render(text_2, True, "white"),
            calculate_centered_position(text_2, WIDTH // 2, HEIGHT // 5 - 30),
        )

        self.screen.blit(
            font.render(text_3, True, "white"),
            calculate_centered_position(text_3, WIDTH // 2, HEIGHT // 1.5),
        )

    def play(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.show_controls:
                            self.show_controls = False
                        else:
                            pygame.quit()
                            quit()
                    if event.key == pygame.K_RETURN:
                        self.sounds["select"].play()
                        if self.is_start_game_selected:
                            self.is_running = False
                        else:
                            self.show_controls = True
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
