import pygame
import sys
from internal.settings import *
from internal.draw import *


def main():
    pygame.init()
    font = pygame.font.SysFont('Arial', 30)
    pygame.display.set_caption("My Game")
    pygame.font.init()

    game = Game(font)

    game.run_game()

    game.save_clicks()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
