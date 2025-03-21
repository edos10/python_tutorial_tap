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
    {"top_text": "Распечатать текст", "center_text": ["print('Hello world!')"]},
    {"top_text": "Ввести имя и распечатать", "center_text": ["name = input()", "print('Здравствуйте, ' + name + '!')", ""]},
    {"top_text": "Не все так очевидно", "center_text": ["a = input()", "b = input()", "print(a + b) - выведет не сумму"]},
    {"top_text": "Типы данных", "center_text": ["a = 5", 'b = 7', 'print(a + b) - так правильно']},
    {"top_text": "Повторим ввод", "center_text": ["a = int(input())", 'b = int(input())', 'print(a + b) - тоже ок']},
    {"top_text": "Арифметика", "center_text": ["a + b", 'a - b', 'a * b', 'a / b', 'a ** b - a ^ b']},
    {"top_text": "Продвинутая арифметика", "center_text": ['a // b - нацело', 'a / b - с остатком']},
    {"top_text": "условие", "center_text": ["if x > 0:", '    print(x)', 'else:', '    print(-x)']},
    {"top_text": "Вложенное условие", "center_text": ["if x > 0:", '    if y > 0: ', '        print("ok")']},
    {"top_text": "Сравнение", "center_text": [">, < - Больше меньше", '>= <= Больше или равно']},
    {"top_text": "Сравнение 2", "center_text": ["== - равно", '!= - не равно']},
    {"top_text": "Bool", "center_text": ["Тип данных", 'Верно или неверно']},
    {"top_text": "Логика", "center_text": ["and - и", 'or - или']},
    {"top_text": "На практике", "center_text": ["if a % 10 == 0 or b % 10 == 0:", '    print("YES")']},
    {"top_text": "Каскадные условия", "center_text": ["if x > 0 and y > 0:", '    print("Первая четверть")', 'elif x > 0 and y < 0:', '    print("Четвертая четверть")']},
    {"top_text": "Дробные числа", "center_text": ["x = float(input())", 'print(x)']},
    {"top_text": "Циклы", "center_text": ["for i in 1, 2, 3, 'one', 'two', 'three':", '    print(i)']},
    {"top_text": "range", "center_text": ["for i in range(4):", '    print(i) - 0 1 2 3']},
    {"top_text": "range со стартом", "center_text": ["for i in range(1, 4)", '    print(i) - 1 2 3']},
    {"top_text": "range с шагом", "center_text": ["for i in range(1, 4, 2)", '    print(i) - 1 3']},
    {"top_text": "Разделитель", "center_text": ["print(1, 2, 3, sep=', ')"]},
    {"top_text": "Slice", "center_text": ["s = 'abcdefg'", 'print(s[1]) - b', 'print(s[-1]) -  g', 'print(s[1:3]) - bc']},
    {"top_text": "Поиск номера вхождения", "center_text": ["S.find('e')"]},
    {"top_text": "Замена", "center_text": ["print('Hello'.replace('l', 'L'))"]},
    {"top_text": "Посчитать вхождения", "center_text": ["print(('a' * 10).count('aa'))"]},
    {"top_text": "Цикл while", "center_text": ["i = 1", 'while i <= 10:', '    print(i ** 2)', '    i += 1']},
    {"top_text": "Прерывание", "center_text": ["break - завершить цикл"]},
    {"top_text": "Списки", "center_text": ["a = [1, 2, 3]", 'b = [4, 5]']},
    {"top_text": "Доступ к элементу", "center_text": ["a = [1, 2, 3]", 'print(a[1])']},
    {"top_text": "Обход списка", "center_text": ["a = [1, 2, 3, 4, 5]", 'for elem in a:', '    print(elem, end=' ')']},
    {"top_text": "split - сделать массив", "center_text": ["a = input().split()", "a = '192.168.0.1'.split('.')"]},
    {"top_text": "Операции", "center_text": ["max,  min", 'in, not in']},
    {"top_text": "Функции", "center_text": ["def max(a, b):", '    if a > b:', '        return a', '    return b']},
    {"top_text": "Рекурсия", "center_text": ["def f(n):", '    if n == 0:', '        return 1', '    else:', '        return n * f(n - 1)']},
    {"top_text": "Глобальная переменная", "center_text": ["a = 0", 'def f():', '    global a']},
    {"top_text": "Двумерный массив", "center_text": ["a = [[1, 2, 3], [4, 5, 6]]", 'print(a[0]) - первый массив', 'print(a[0][2]) - 6']},
    {"top_text": "Генератор 2d", "center_text": ["a = [[0] * m] * n", '[[0] * m for i in range(n)]']},
    {"top_text": "Ввод 2d", "center_text": ["a = [[int(j) for j in input().split()] for i in range(n)]"]},
    {"top_text": "Set", "center_text": ["A = {1, 2, 3}", 'B = {3, 2, 3, 1} - A = B', 'A = set("qwerty")']},
    {"top_text": "Операции", "center_text": ["A.union(B)", 'A.intersection(B)', 'A.update(B)', 'A.difference(B)']},
    {"top_text": "Словарь", "center_text": ["Capitals = dict()", "Capitals['Russia'] = 'Moscow'"]},
    {"top_text": "проверка наличия", "center_text": ["if key in A:", '    del A[key]']},
    {"top_text": "Перебор", "center_text": ["for key in A:", '    print(key, A[key])']},
    {"top_text": "Перебор 2", "center_text": ["for key, val in A.items():", '    print(key, val)']},
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
