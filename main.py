import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Kombat")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 139)
YELLOW = (255, 223, 0)  # Ярко-желтый
DARK_YELLOW = (204, 170, 0)  # Темный желтый
DARK_RED = (139, 0, 0)  # Темно-красный для кнопок
DARK_PURPLE = (48, 25, 52)  # Темно-фиолетовый для градиента
LIGHT_GRAY = (211, 211, 211)  # Светло-серый для текста
GREEN = (0, 255, 0)

# Шрифты
font = pygame.font.SysFont('Arial', 30)

# Уровни
levels = [
    {"top_text": "Уровень 1", "center_text": ["Привет! Это первый уровень.", "       Кликай, чтобы увидеть текст."]},
    {"top_text": "Уровень 2", "center_text": ["Второй уровень.", "Здесь текст длиннее.", "Продолжай кликать!"]},
    {"top_text": "Уровень 3", "center_text": ["Третий уровень.", "Это последний уровень.", "Спасибо за игру!"]},
    {"top_text": "Уровень 4", "center_text": ["name = input()", 'print(f"Hello, {name}!")']},
    {"top_text": "Уровень 5", "center_text": ["wow", 'hey']},
    {"top_text": "Уровень 6", "center_text": ["wow", 'hey']},
    {"top_text": "Уровень 7", "center_text": ["wow", 'hey']},
    {"top_text": "Уровень 8", "center_text": ["wow", 'hey']},
    {"top_text": "Уровень 9", "center_text": ["wow", 'hey']},
    {"top_text": "Уровень 10", "center_text": ["wow", 'hey']}
]

# Переменные
current_level = None
current_theme = 1
clicks = 0
displayed_text = ""
text_index = 0
letter_index = 0
level_offset = 0  # Для отслеживания текущего смещения уровня в списке

def load_clicks():
    global clicks
    try:
        f = open("clicks.txt", "r")
        click_file = [int(i) for i in f.readlines()]
        clicks = max(click_file)
    except Exception:
        pass


def load_levels():
    try:
        f = open("levels.txt", "r")
        level_from_file = [int(j) for j in f.readlines()]
        return level_from_file
    except Exception:
        return []

levels_done = load_levels()


def is_done_level(level: int):
    global levels_done
    return level + 1 in levels_done


load_clicks()


# Функция для отрисовки текста
def draw_text(text, x, y, color=LIGHT_GRAY):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Функция для отрисовки кнопки
def draw_button(text, x, y, width, height, button_color, text_color):
    pygame.draw.rect(screen, button_color, (x, y, width, height), border_radius=10)
    draw_text(text, x + width // 2, y + height // 2, color=text_color)

# Функция для отрисовки градиентного фона
def draw_gradient_background(first_color, second_color):
    for i in range(SCREEN_HEIGHT):
        # Градиент от черного к темно-красному
        color = (
            int(first_color[0] * i / SCREEN_HEIGHT + second_color[0] * (1 - i / SCREEN_HEIGHT)),
            int(first_color[1] * i / SCREEN_HEIGHT + second_color[1] * (1 - i / SCREEN_HEIGHT)),
            int(first_color[2] * i / SCREEN_HEIGHT + second_color[2] * (1 - i / SCREEN_HEIGHT)),
        )
        pygame.draw.line(screen, color, (0, i), (SCREEN_WIDTH, i))

# Функция для отрисовки меню выбора уровня
def draw_level_menu():
    first_color = DARK_RED
    second_color = BLACK
    button_color = DARK_YELLOW
    text_color = BLACK
    if current_theme == 1:
        first_color = DARK_PURPLE
        second_color = BLACK
        button_color = DARK_BLUE
        text_color = WHITE
    draw_gradient_background(first_color, second_color)  # Градиентный фон
    draw_text("Выберите уровень", SCREEN_WIDTH // 2, 50, color=WHITE)  # Желтый текст

    # Отображаем 5 уровней за раз
    prev_color_button = button_color
    for i in range(level_offset, min(level_offset + 5, len(levels))):
        if is_done_level(i):
            button_color = GREEN
        else:
            button_color = prev_color_button
        draw_button(levels[i]["top_text"], SCREEN_WIDTH // 2 - 100, 150 + (i - level_offset) * 100, 200, 50, button_color, text_color)

    # Кнопки для прокрутки
    if level_offset > 0:
        draw_button("←", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 100, 50, 50, button_color, text_color)  # Левая кнопка
    if level_offset + 5 < len(levels):
        draw_button("→", SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT - 100, 50, 50, button_color, text_color)  # Правая кнопка

    #  Смена темы
    if current_theme == 1:
        draw_button("X", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 560, 50, 50, DARK_PURPLE, text_color)
        draw_button("", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 500, 50, 50, DARK_RED, text_color)
    else:
        draw_button("", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 560, 50, 50, DARK_PURPLE, text_color)
        draw_button("X", SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 500, 50, 50, DARK_RED, text_color)

    draw_button("Выход", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50, button_color, text_color)
    pygame.display.flip()

# Функция для отрисовки уровня
def draw_level():
    first_color = DARK_RED
    second_color = BLACK
    button_color = DARK_YELLOW
    text_color = WHITE
    if current_theme == 1:
        first_color = DARK_PURPLE
        second_color = BLACK
        button_color = DARK_BLUE
        text_color = WHITE
    draw_gradient_background(first_color, second_color)  # Градиентный фон
    draw_text(levels[current_level]["top_text"], SCREEN_WIDTH // 2, 50, color=text_color)  # Желтый текст

    if text_index < len(levels[current_level]["center_text"]):
        for i in range(text_index + 1):
            current_text = levels[current_level]["center_text"][i]
            if i == text_index:
                if letter_index < len(current_text):
                    letter_surface = font.render(current_text[:letter_index], True, text_color)
                    screen.blit(letter_surface, (250, 100 + i * 40))
            else:
                letter_surface = font.render(current_text, True, text_color)
                screen.blit(letter_surface, (250, 100 + i * 40))

    draw_button("Клик!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 150, 200, 100, button_color, text_color)
    draw_button("Меню", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50, button_color, text_color)
    draw_text(f"Кликов: {clicks}", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200, color=button_color)
    pygame.display.flip()


def save_clicks(click: int):
    with open("clicks.txt", "a+") as f:
        f.write(f"{click}\n")


def save_level(level: int):
    global levels_done

    levels_done += [level]

    with open("levels.txt", "a+") as f:
        f.write(f"{level}\n")


# Основной цикл игры
running = True
in_menu = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if in_menu:
                # Обработка кликов в меню
                for i in range(level_offset, min(level_offset + 5, len(levels))):
                    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 150 + (i - level_offset) * 100, 200, 50)
                    if button_rect.collidepoint(mouse_pos):
                        current_level = i
                        displayed_text = ""
                        in_menu = False
                        text_index = 0
                        letter_index = 0
                # Кнопка выхода
                exit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50)
                if exit_button_rect.collidepoint(mouse_pos):
                    running = False
                # Кнопки прокрутки
                left_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 100, 50, 50)
                if left_button_rect.collidepoint(mouse_pos) and level_offset > 0:
                    level_offset -= 5

                right_button_rect = pygame.Rect(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT - 100, 50, 50)
                if right_button_rect.collidepoint(mouse_pos) and level_offset + 5 < len(levels):
                    level_offset += 5
                # Кнопки смены темы
                first_theme_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 500, 50, 50)
                if first_theme_button_rect.collidepoint(mouse_pos):
                    current_theme = 0
                second_theme_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 560, 50, 50)
                if second_theme_button_rect.collidepoint(mouse_pos):
                    current_theme = 1
            else:
                # Обработка кликов в уровне
                click_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 150, 200, 100)
                menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50)
                if click_button_rect.collidepoint(mouse_pos):
                    clicks += 1
                    save_clicks(clicks)
                    if text_index < len(levels[current_level]["center_text"]):
                        if letter_index < len(levels[current_level]["center_text"][text_index]) - 1:
                            letter_index += 1
                        else:
                            text_index += 1
                            letter_index = 0
                    else:
                        save_level(current_level+1)

                    if len(displayed_text) < len(levels[current_level]["center_text"]):
                        displayed_text += levels[current_level]["center_text"][len(displayed_text)]

                elif menu_button_rect.collidepoint(mouse_pos):
                    in_menu = True

    if in_menu:
        draw_level_menu()
    else:
        draw_level()

# Завершение работы
pygame.quit()
save_clicks(clicks)
sys.exit()
