import pygame
from settings import WIDTH, HEIGHT, FPS, TILE_SIZE

pygame.font.init()

font = pygame.font.Font("./font/Minecraft.ttf", 34)


def calculate_centered_position(text: str, x: int, y: int):
    text_width, text_height = font.size(text)
    return (x - text_width // 2, y - text_height // 2)


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.is_running = True

    def draw(self):
        text_1 = "Scribbles vs. Sketches"
        text_2 = "Press enter to start..."
        text_3 = "Team One Games' second project."

        # make the background an image
        background_image = pygame.image.load("images/background.png")
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        self.screen.blit(background_image, (0, 0))

        self.screen.blit(
            font.render(text_1, True, "white"),
            calculate_centered_position(
                text_1, WIDTH // 2, HEIGHT // 2 - TILE_SIZE * 5
            ),
        )
        self.screen.blit(
            font.render(text_2, True, "white"),
            calculate_centered_position(
                text_2, WIDTH // 2, HEIGHT // 2 - TILE_SIZE * 3
            ),
        )
        self.screen.blit(
            font.render(text_3, True, "white"),
            calculate_centered_position(text_3, WIDTH // 2, HEIGHT // 2),
        )

    def play(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_RETURN:
                        self.is_running = False

            self.draw()

            pygame.display.update()  # update the display
