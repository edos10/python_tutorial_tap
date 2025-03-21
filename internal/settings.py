import pygame

# Настройки экрана
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
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
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)