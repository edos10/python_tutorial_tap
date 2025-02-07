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
YELLOW = (255, 223, 0)  # Ярко-желтый
DARK_YELLOW = (204, 170, 0)  # Темный желтый
DARK_RED = (139, 0, 0)  # Темно-красный для кнопок
DARK_PURPLE = (48, 25, 52)  # Темно-фиолетовый для градиента
LIGHT_GRAY = (211, 211, 211)  # Светло-серый для текста

# Шрифты
font = pygame.font.SysFont('Arial', 30)

# Уровни
levels = [
    {"top_text": "Уровень 1", "center_text": ["Привет! Это первый уровень.", "       Кликай, чтобы увидеть текст."]},
    {"top_text": "Уровень 2", "center_text": ["Второй уровень.", "Здесь текст длиннее.", "Продолжай кликать!"]},
    {"top_text": "Уровень 3", "center_text": ["Третий уровень.", "Это последний уровень.", "Спасибо за игру!"]},
    # Новый уровень
    {"top_text": "Уровень 4", "center_text": ["name = input()", 'print(f"Hello, {name}!")']}  # Новый текст для нового уровня
]

# Переменные
current_level = None
clicks = 0
displayed_text = ""
text_index = 0
letter_index = 0


# Функция для отрисовки текста
def draw_text(text, x, y, color=LIGHT_GRAY):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# Функция для отрисовки кнопки
def draw_button(text, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)
    draw_text(text, x + width // 2, y + height // 2, color=BLACK)  # Белый текст для контраста


# Функция для отрисовки градиентного фона
def draw_gradient_background():
    for i in range(SCREEN_HEIGHT):
        # Градиент от черного к темно-красному
        color = (
            int(DARK_RED[0] * i / SCREEN_HEIGHT + BLACK[0] * (1 - i / SCREEN_HEIGHT)),
            int(DARK_RED[1] * i / SCREEN_HEIGHT + BLACK[1] * (1 - i / SCREEN_HEIGHT)),
            int(DARK_RED[2] * i / SCREEN_HEIGHT + BLACK[2] * (1 - i / SCREEN_HEIGHT)),
        )
        pygame.draw.line(screen, color, (0, i), (SCREEN_WIDTH, i))


# Функция для отрисовки меню выбора уровня
def draw_level_menu():
    draw_gradient_background()  # Градиентный фон
    draw_text("Выберите уровень", SCREEN_WIDTH // 2, 50, color=YELLOW)  # Желтый текст
    for i, level in enumerate(levels):
        draw_button(level["top_text"], SCREEN_WIDTH // 2 - 100, 150 + i * 100, 200, 50, DARK_YELLOW)
    draw_button("Выход", SCREEN_WIDTH // 2 - 100, 150 + len(levels) * 100, 200, 50, DARK_YELLOW)
    pygame.display.flip()


# Функция для отрисовки уровня
def draw_level():
    draw_gradient_background()  # Градиентный фон
    draw_text(levels[current_level]["top_text"], SCREEN_WIDTH // 2, 50, color=YELLOW)  # Желтый текст

    if text_index < len(levels[current_level]["center_text"]):
        for i in range(text_index + 1):
            current_text = levels[current_level]["center_text"][i]
            if i == text_index:
                if letter_index < len(current_text):
                    letter_surface = font.render(current_text[:letter_index], True, YELLOW)
                    screen.blit(letter_surface, (250, 100 + i * 40))
            else:
                letter_surface = font.render(current_text, True, YELLOW)
                screen.blit(letter_surface, (250, 100 + i * 40))

    draw_button("Клик!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 150, 200, 100, YELLOW)
    draw_button("Меню", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50, YELLOW)
    draw_text(f"Кликов: {clicks}", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200, color=YELLOW)
    pygame.display.flip()


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
                for i, level in enumerate(levels):
                    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 150 + i * 100, 200, 50)
                    if button_rect.collidepoint(mouse_pos):
                        current_level = i
                        displayed_text = ""
                        in_menu = False
                        text_index = 0
                        letter_index = 0
                # Кнопка выхода
                exit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 150 + len(levels) * 100, 200, 50)
                if exit_button_rect.collidepoint(mouse_pos):
                    running = False
            else:
                # Обработка кликов в уровне
                click_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 150, 200, 100)
                menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 50, 200, 50)
                if click_button_rect.collidepoint(mouse_pos):
                    clicks += 1
                    if text_index < len(levels[current_level]["center_text"]):
                        if letter_index < len(levels[current_level]["center_text"][text_index]) - 1:
                            letter_index += 1
                        else:
                            text_index += 1
                            letter_index = 0

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
sys.exit()
