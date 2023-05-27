import time
import pygame
import math

from mainmenu import font
from settings import FPS, HEIGHT, WIDTH, maps, map_names


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
            except:
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
            self.update()
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
            self.draw()
            self.write_texts()
            self.update_screen()


class cutscene1(Cutscene):
    def __init__(self):
        super().__init__()
        self.createActor("images/background.png", 0, 0, WIDTH, HEIGHT)
        self.carnak = self.createActor("sprites/carnak.png", WIDTH, 258, 128, 128)
        self.marcos = self.createActor("sprites/marcos1.png", WIDTH // 5, 715, 128, 128)

        img_with_flip = pygame.transform.flip(self.marcos.image, True, False)

        self.marcos.image = img_with_flip

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


class mapselection(Cutscene):
    def __init__(self):
        super().__init__()
        self.createActor("images/background_controls.png", 0, 0, WIDTH, HEIGHT)

        self.level_idx = 1

        self.is_pressed = False

        self.map1 = self.createActor("images/map_1.png", 115, 165, 335, 335)
        self.map2 = self.createActor("images/map_2.png", 480, 165, 335, 335)
        self.map3 = self.createActor("images/map_3.png", 115, 550, 335, 335)
        self.map4 = self.createActor("images/map_4.png", 480, 550, 335, 335)

        self.rectangle = self.createActor("images/rectangle.png", 115, 165, 350, 350)

        self.map_name = self.createText(
            map_names[self.level_idx - 1], WIDTH // 2, HEIGHT - 30, "white"
        )

        self.title = self.createText("Select a map", WIDTH // 2, 80, "white")

    def increase_level_idx(self):
        if self.level_idx >= len(maps):
            return

        self.level_idx += 1

    def decrease_level_idx(self):
        if self.level_idx <= 1:
            return

        self.level_idx -= 1

    def decrease_two_levels_idx(self):
        if self.level_idx <= 2:
            return

        self.level_idx -= 2

    def increase_two_levels_idx(self):
        if self.level_idx >= len(maps) - 1:
            return

        self.level_idx += 2

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if not self.is_pressed:
                self.decrease_level_idx()
                self.is_pressed = True
        elif keys[pygame.K_UP]:
            if not self.is_pressed:
                self.decrease_two_levels_idx()
                self.is_pressed = True
        elif keys[pygame.K_DOWN]:
            if not self.is_pressed:
                self.increase_two_levels_idx()
                self.is_pressed = True
        elif keys[pygame.K_RIGHT]:
            if not self.is_pressed:
                self.increase_level_idx()
                self.is_pressed = True
        elif keys[pygame.K_x]:
            return True
        else:
            self.is_pressed = False

        return False

    def update(self):
        # draw a rectangle around the selected map

        if self.level_idx == 1:
            self.rectangle.rect.x = 115 - 5
            self.rectangle.rect.y = 165 - 5
        elif self.level_idx == 2:
            self.rectangle.rect.x = 480 - 5
            self.rectangle.rect.y = 165 - 5
        elif self.level_idx == 3:
            self.rectangle.rect.x = 115 - 5
            self.rectangle.rect.y = 550 - 5
        elif self.level_idx == 4:
            self.rectangle.rect.x = 480 - 5
            self.rectangle.rect.y = 550 - 5

        self.map_name.text = map_names[self.level_idx - 1]

        if self.get_input():  # map selected
            self.is_running = False


class credits(Cutscene):
    def __init__(self):
        super().__init__()
        texts = [
            "Made by Binder & Marcelo",
            "Programming: Binder & Marcelo"
            "Art: Arthur & Leo",
            "Testing: Fenoxer",
            "The Amazing Cutscene System: Binder",
            "Cutscenes: Marcelo",
            "Level Design: Binder",
            "Made with 1006 lines of code",
            "Bday boys: Marcos & Daniel",
        ]

        for i in range(len(texts)):
            self.createText(texts[i], WIDTH / 2, HEIGHT + i * (HEIGHT) / 2, "white")
        self.createText(
            "THE END", WIDTH / 2, HEIGHT + (len(texts) + 2) * (HEIGHT) / 2, "white"
        )

        self.y = 0

    def update(self):
        for i in self.texts:
            i.y -= 5
        
        self.y += 1

        if self.y > 1200:
            self.is_running = False


class celebration(Cutscene):
    def __init__(self, winner):
        super().__init__()
        self.createActor("sprites/" + winner + "1.png", 128, 128, WIDTH, HEIGHT)
        self.createText(
            "VICTORY " + winner.upper(), (WIDTH / 2) - 200, HEIGHT / 2 + 200, "white"
        )

        self.music = pygame.mixer.Sound("sounds/victory.mp3")
        self.music.play()

    def update(self):
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
                    credits().play()
                    self.is_running = False
                    self.music.stop()
