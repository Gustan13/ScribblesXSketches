import time
import pygame
import math

from mainmenu import font
from settings import FPS, HEIGHT, WIDTH


class Cutscene:
    class Actor:
        def __init__(self, name, x, y, width, height):
            try:
                self.image = pygame.image.load(name).convert_alpha()
                self.image = pygame.transform.scale(self.image, (width, height))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.type = "image_file"
            except pygame.error:
                self.image = name
                self.rect = pygame.Rect(x, y, width, height)
                self.type = "solid_color"

    class Text:
        def __init__(self, string, x, y, color):
            self.text = string
            self.x = x
            self.y = y
            self.color = color

    def __init__(self):
        self.is_running = True
        self.screen = pygame.display.get_surface()
        self.actors = []
        self.texts = []
        self.clock = pygame.time.Clock()

    def createActor(self, name, x, y, width, height):
        actor = self.Actor(name, x, y, width, height)
        self.actors.append(actor)
        return actor

    def createText(self, string, x, y, color):
        text = self.Text(string, x, y, color)
        self.texts.append(text)
        return text

    def move_to(self, rect, x, y, percentage):
        if abs(x - rect.x) < percentage and abs(y - rect.y) < percentage:
            return True

        hip = math.sqrt((x - rect.x) ** 2 + (y - rect.y) ** 2)

        rect.x += percentage * (x - rect.x) / hip
        rect.y += percentage * (y - rect.y) / hip

        return False

    def first_timer(self, time):
        if time <= 0:
            return True

        time -= 1
        return False

    def rotate(self, surface, angle):
        return pygame.transform.rotate(surface, angle)

    def draw(self):
        for i in self.actors:
            if i.type == "image_file":
                self.screen.blit(i.image, i.rect)
            else:
                pygame.draw.rect(self.screen, i.image, i.rect)

    def write_texts(self):
        for i in self.texts:
            self.screen.blit(
                font.render(i.text, True, i.color),
                self.calculate_text_position(i.text, i.x, i.y),
            )

    def calculate_text_position(self, text, x, y):
        text_width, text_height = font.size(text)
        return (x - text_width / 2, y - text_height / 2)

    def get_text_size(self, text):
        return font.size(text)

    def update_screen(self):
        self.clock.tick(FPS)
        pygame.display.update()

    def play(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if (
                        event.key == pygame.K_ESCAPE
                        or event.key == pygame.K_SPACE
                        or event.key == pygame.K_RETURN
                    ):
                        self.is_running = False

            self.screen.fill("black")
            self.update()
            self.draw()
            self.write_texts()
            self.update_screen()


class cutscene1(Cutscene):
    def __init__(self):
        super().__init__()
        self.createActor("images/background.png", 0, 0, WIDTH, HEIGHT)
        self.carnak = self.createActor("sprites/carnak.png", WIDTH, 258, 128, 128)
        self.marcos = self.createActor("sprites/marcos1.png", WIDTH // 5, 715, 128, 128)
        self.daniel = self.createActor(
            "sprites/daniel1.png", 4 * WIDTH // 5, 715, 128, 128
        )

        self.first_timer = FPS * 3.5
        self.second_timer = FPS * 2.5

        self.createText("Press enter to skip...", WIDTH - 200, HEIGHT - 50, "white")

    def update(self):
        if not self.move_to(self.carnak.rect, WIDTH // 2 - 56, self.carnak.rect.y, 5):
            return

        self.createText(
            "Do you want to be the best illustrators in the world?",
            WIDTH // 2,
            50,
            "white",
        )

        if self.first_timer > 0:
            self.first_timer -= 1
            return

        self.createText("Yes.", WIDTH // 5 + 55, 666, "white")
        self.createText("Yes.", 4 * WIDTH // 5 + 55, 666, "white")

        if self.second_timer > 0:
            self.second_timer -= 1
            return

        self.createText(
            "Then you have to sign this contract.", WIDTH // 2, 100, "white"
        )


class cutscene2(Cutscene):
    def __init__(self):
        super().__init__()
        self.createActor("images/background.png", 0, 0, WIDTH, HEIGHT)
        self.contract = self.createActor(
            "images/Contrato.png",
            WIDTH // 2 - WIDTH // 1.2 // 2,
            HEIGHT // 2 - HEIGHT // 1.2 // 2,
            WIDTH // 1.2,
            HEIGHT // 1.2,
        )
        self.first_timer = FPS * 2.5
        self.second_timer = FPS * 2.5

        self.createText("Press enter to skip...", WIDTH - 200, HEIGHT - 50, "white")

    def update(self):
        if self.first_timer > 0:
            self.first_timer -= 1
            return

        self.createText(
            "MARCOS",
            self.contract.rect.x + 280,
            self.contract.rect.y + self.contract.rect.height - 150,
            (95, 73, 44),
        )

        if self.second_timer > 0:
            self.second_timer -= 1
            return

        self.createText(
            "DANIEL",
            # right side of the contract - 265
            self.contract.rect.x + self.contract.rect.width - 320,
            self.contract.rect.y + self.contract.rect.height - 150,
            (95, 73, 44),
        )


class cutscene3(Cutscene):
    def __init__(self):
        super().__init__()
        self.createActor("images/background.png", 0, 0, WIDTH, HEIGHT)

        self.createText(
            "Now, only the best illustrator will survive...", WIDTH // 2, 50, "white"
        )

        self.createActor("sprites/carnak.png", WIDTH // 2 - 56, 258, 128, 128)

        self.createText("Press enter to skip...", WIDTH - 200, HEIGHT - 50, "white")

    def update(self):
        pass


class credits(Cutscene):
    def __init__(self):
        super().__init__()
        texts = [
            "Made by Binder & Marcelo",
            "Pixel Art: Marcelo",
            "Enemy Pathfinding: Binder",
            "Art work feedback: Marcos A.K.A Dudu",
            "Player movement: Marcelo",
            "Testing: Fenoxer",
            "Level System: Binder",
            "Rendering System: Marcelo",
            "Cutscene System: Binder",
            "Cutscenes: Marcelo",
            "Level Design: Binder",
            "Made with 1006 lines of code",
            "Bday boy: Leo",
        ]

        for i in range(len(texts)):
            self.createText(texts[i], WIDTH / 2, HEIGHT + i * (HEIGHT) / 2, "white")
        self.createText(
            "THE END", WIDTH / 2, HEIGHT + (len(texts) + 2) * (HEIGHT) / 2, "white"
        )

    def update(self):
        for i in self.texts:
            i.y -= 5
