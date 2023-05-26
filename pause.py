import pygame
from mainmenu import font, big_font
from settings import HEIGHT, WIDTH


class Pause:
    def __init__(self, screen):
        self.screen = screen
        self.pause_text = font.render("Pause", True, (95, 73, 44))
        self.resume_text = font.render("Resume", True, (95, 73, 44))
        self.options_text = font.render("Options", True, (95, 73, 44))
        self.main_menu_text = font.render("Main Menu", True, (95, 73, 44))
        self.cursor = big_font.render(">", True, (95, 73, 44))
        self.background = pygame.image.load("images/Contrato_em_branco.png")

        # increase the size of the background image
        self.background = pygame.transform.scale(
            self.background, (WIDTH // 1.25, HEIGHT // 1.25)
        )
        self.background_rect = self.background.get_rect()
        self.background_rect.center = (WIDTH // 2, HEIGHT // 2)

        self.pause_text_rect = self.pause_text.get_rect()
        self.pause_text_rect.center = (WIDTH // 2, HEIGHT // 2)

        self.cursor_rect = self.pause_text_rect.copy()
        self.cursor_rect.left -= self.cursor.get_width() * 1.5

        offset = self.background.get_height() // 6

        self.pause_text_rect.top = self.background_rect.top + 64

        self.options_text_rect = self.options_text.get_rect()

        # resume text rect is the same as pause with offset added to the y
        self.resume_text_rect = self.pause_text_rect.copy()
        self.resume_text_rect.top += offset

        # options text rect is the same as resume with offset added to the y
        self.options_text_rect = self.resume_text_rect.copy()
        self.options_text_rect.top += offset

        # main menu text rect is the same as options with offset added to the y
        self.main_menu_text_rect = self.options_text_rect.copy()
        self.main_menu_text_rect.top += offset

        self.selected_state = 0

    def draw(self):
        """Draws the pause menu"""
        self.screen.blit(self.background, self.background_rect)

        self.screen.blit(self.pause_text, self.pause_text_rect)
        self.screen.blit(self.resume_text, self.resume_text_rect)
        self.screen.blit(self.options_text, self.options_text_rect)
        self.screen.blit(self.main_menu_text, self.main_menu_text_rect)
        self.screen.blit(self.cursor, self.cursor_rect)

    def update(self):
        """Updates the state of the pause menu"""
        if self.selected_state == 0:
            self.cursor_rect.top = self.resume_text_rect.top
        elif self.selected_state == 1:
            self.cursor_rect.top = self.options_text_rect.top
        elif self.selected_state == 2:
            self.cursor_rect.top = self.main_menu_text_rect.top

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_cursor_up()
                elif event.key == pygame.K_DOWN:
                    self.move_cursor_down()
                elif event.key == pygame.K_RETURN:
                    if self.selected_state == 0:
                        return "resume"
                    elif self.selected_state == 1:
                        return "options"  # TODO: Make this a trolling
                    elif self.selected_state == 2:
                        return "main_menu"
                elif event.key == pygame.K_ESCAPE:
                    return "resume"
            elif event.type == pygame.QUIT:
                return "quit"

    def move_cursor_up(self):
        """Moves the cursor up one state"""
        self.selected_state -= 1
        if self.selected_state < 0:
            self.selected_state = 2

    def move_cursor_down(self):
        """Moves the cursor down one state"""
        self.selected_state += 1
        if self.selected_state > 2:
            self.selected_state = 0
