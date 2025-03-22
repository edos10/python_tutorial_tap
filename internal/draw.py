# Переменные
from internal.settings import *
import json

class Game:
    def __init__(self, font=None,
                 clicks_file="clicks.txt",
                 levels_file="levels.txt",
                 path_levels="./info/levels.json"
                 ):
        self.current_level = None
        self.current_theme = 1
        self.clicks = 0
        self.displayed_text = ""
        self.text_index = 0
        self.letter_index = 0
        self.level_offset = 0  # Для отслеживания текущего смещения уровня в списке
        self.levels = []
        self.levels_done = []

        self.running = True
        self.in_menu = True

        self.clicks_file = clicks_file
        self.levels_file = levels_file
        self.path_levels = path_levels

        self.font = font
        self.screen = screen

        self.load_levels()
        self.load_clicks()
        self.load_completed_levels()

    def load_levels(self):
        with open(self.path_levels, 'r', encoding='utf-8') as file:
            self.levels = json.load(file)

    def load_clicks(self):
        try:
            f = open(self.clicks_file, "r")
            click_file = [int(i) for i in f.readlines()]
            self.clicks = max(click_file)
        except Exception:
            pass

    def load_completed_levels(self):
        try:
            f = open(self.levels_file, "r")
            self.levels_done = [int(j) for j in f.readlines()]
        except Exception:
            return []

    def is_done_level(self, level: int):
        return level + 1 in self.levels_done

    # Функция для отрисовки текста
    def draw_text(self, text, x, y, color=LIGHT_GRAY):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    # Функция для отрисовки кнопки
    def draw_button(self, text, x, y, width, height, button_color, text_color):
        pygame.draw.rect(self.screen, button_color, (x, y, width, height), border_radius=10)
        self.draw_text(text, x + width // 2, y + height // 2, color=text_color)

    # Функция для отрисовки градиентного фона
    def draw_gradient_background(self, first_color, second_color):
        for i in range(SCREEN_HEIGHT):
            # Градиент от черного к темно-красному
            color = (
                int(first_color[0] * i / SCREEN_HEIGHT + second_color[0] * (1 - i / SCREEN_HEIGHT)),
                int(first_color[1] * i / SCREEN_HEIGHT + second_color[1] * (1 - i / SCREEN_HEIGHT)),
                int(first_color[2] * i / SCREEN_HEIGHT + second_color[2] * (1 - i / SCREEN_HEIGHT)),
            )
            pygame.draw.line(self.screen, color, (0, i), (SCREEN_WIDTH, i))

    # Функция для отрисовки меню выбора уровня
    def draw_level_menu(self):
        first_color = DARK_RED
        second_color = BLACK
        button_color = DARK_YELLOW
        text_color = BLACK
        if self.current_theme == 1:
            first_color = DARK_PURPLE
            second_color = BLACK
            button_color = DARK_BLUE
            text_color = WHITE
        self.draw_gradient_background(first_color, second_color)  # Градиентный фон
        self.draw_text("Выберите уровень", SCREEN_WIDTH // 2, 50, color=WHITE)  # Желтый текст

        # Отображаем 5 уровней за раз
        prev_color_button = button_color
        for i in range(self.level_offset, min(self.level_offset + 5, len(self.levels))):
            if self.is_done_level(i):
                button_color = GREEN
            else:
                button_color = prev_color_button
            self.draw_button(self.levels[i]["top_text"], SCREEN_WIDTH // 2 - 100, 150 + (i - self.level_offset) * 100, 400, 50, button_color, text_color)

        # Кнопки для прокрутки
        if self.level_offset > 0:
            self.draw_button("←", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 100, 50, 50, button_color, text_color)  # Левая кнопка
        if self.level_offset + 5 < len(self.levels):
            self.draw_button("→", SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT - 100, 50, 50, button_color, text_color)  # Правая кнопка

        #  Смена темы
        if self.current_theme == 1:
            self.draw_button("X", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 560, 50, 50, DARK_PURPLE, text_color)
            self.draw_button("", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 500, 50, 50, DARK_RED, text_color)
        else:
            self.draw_button("", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 560, 50, 50, DARK_PURPLE, text_color)
            self.draw_button("X", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 500, 50, 50, DARK_RED, text_color)

        self.draw_button("Выход", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50, button_color, text_color)
        pygame.display.flip()

    # Функция для отрисовки уровня
    def draw_level(self):

        first_color = DARK_RED
        second_color = BLACK
        button_color = DARK_YELLOW
        text_color = WHITE
        if self.current_theme == 1:
            first_color = DARK_PURPLE
            second_color = BLACK
            button_color = DARK_BLUE
            text_color = WHITE
        self.draw_gradient_background(first_color, second_color)  # Градиентный фон
        self.draw_text(self.levels[self.current_level]["top_text"], SCREEN_WIDTH // 2, 50, color=text_color)  # Желтый текст

        if self.text_index < len(self.levels[self.current_level]["center_text"]):
            for i in range(self.text_index + 1):
                current_text = self.levels[self.current_level]["center_text"][i]
                if i == self.text_index:
                    if self.letter_index < len(current_text):
                        letter_surface = self.font.render(current_text[:self.letter_index], True, text_color)
                        self.screen.blit(letter_surface, (250, 100 + i * 40))
                else:
                    letter_surface = self.font.render(current_text, True, text_color)
                    self.screen.blit(letter_surface, (250, 100 + i * 40))

        self.draw_button("Клик!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 150, 200, 100, button_color, text_color)
        self.draw_button("Меню", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50, button_color, text_color)
        self.draw_text(f"Кликов: {self.clicks}", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200, color=button_color)
        pygame.display.flip()


    def save_clicks(self):
        with open("clicks.txt", "a+") as f:
            f.write(f"{self.clicks}\n")


    def save_level(self, level: int):

        self.levels_done += [level]

        with open("levels.txt", "a+") as f:
            f.write(f"{level}\n")

    def run_game(self):
        pygame.init()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.in_menu:
                        # Обработка кликов в меню
                        for i in range(self.level_offset, min(self.level_offset + 5, len(self.levels))):
                            button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 150 + (i - self.level_offset) * 100, 200, 50)
                            if button_rect.collidepoint(mouse_pos):
                                self.current_level = i
                                self.displayed_text = ""
                                self.in_menu = False
                                self.text_index = 0
                                self.letter_index = 0
                        # Кнопка выхода
                        exit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50)
                        if exit_button_rect.collidepoint(mouse_pos):
                            self.running = False
                        # Кнопки прокрутки
                        left_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 100, 50, 50)
                        if left_button_rect.collidepoint(mouse_pos) and self.level_offset > 0:
                            self.level_offset -= 5

                        right_button_rect = pygame.Rect(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT - 100, 50, 50)
                        if right_button_rect.collidepoint(mouse_pos) and self.level_offset + 5 < len(self.levels):
                            self.level_offset += 5
                        # Кнопки смены темы
                        first_theme_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 500, 50, 50)
                        if first_theme_button_rect.collidepoint(mouse_pos):
                            self.current_theme = 0
                        second_theme_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 560, 50, 50)
                        if second_theme_button_rect.collidepoint(mouse_pos):
                            self.current_theme = 1
                    else:
                        # Обработка кликов в уровне
                        click_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 150, 200, 100)
                        menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50)
                        if click_button_rect.collidepoint(mouse_pos):
                            self.clicks += 1
                            self.save_clicks()
                            if self.text_index < len(self.levels[self.current_level]["center_text"]):
                                if self.letter_index < len(self.levels[self.current_level]["center_text"][self.text_index]) - 1:
                                    self.letter_index += 1
                                else:
                                    self.text_index += 1
                                    self.letter_index = 0
                            else:
                                self.save_level(self.current_level + 1)

                            if len(self.displayed_text) < len(self.levels[self.current_level]["center_text"]):
                                self.displayed_text += self.levels[self.current_level]["center_text"][len(self.displayed_text)]

                        elif menu_button_rect.collidepoint(mouse_pos):
                            self.in_menu = True

            if self.in_menu:
                self.draw_level_menu()
            else:
                self.draw_level()
