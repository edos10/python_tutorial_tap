from typing import TextIO

import pygame
import sys


class Level:
    def __init__(self, title, solution):
        self.title = title
        self.solution = solution

class ManagerLevels:
    def __init__(self, path="levels.txt"):
        self.levels = self.load_levels_from_txt(path)

    def load_levels_from_txt(self, path: str) -> list:
        try:
            with open(path, "r") as file:
                levels = []
                for line in file:
                    title, solution = line.strip().split(",", 1)
                    levels.append(Level(title.strip(), solution.strip()))
                return levels
        except FileNotFoundError:
            print(f"Error: File '{path}' not found.")
            return []


class Game:
    def __init__(self, width=800, height=600, fps=60, levels_path="levels.txt"):
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)

        self.level_manager = ManagerLevels(levels_path)
        self.levels = self.level_manager.levels

        if not self.levels:
            print("No levels loaded. Exiting.")
            pygame.quit()
            sys.exit()

        self.click_count = 0
        self.current_level = 0
        self.clicked_letters = ""
        self.in_menu = True
        self.is_finished_level = False


    def draw_text(self, surface, text, x, y, color=(0,0,0)):
        text_surface = self.font.render(text, True, color)
        surface.blit(text_surface, (x, y))

    def draw_level(self):
        self.screen.fill(self.WHITE)
        level = self.levels[self.current_level]
        finished_level = len(level.solution) <= len(self.clicked_letters)

        if finished_level:
            self.draw_text(self.screen, "Уровень завершен! Нажмите Enter для продолжения", self.width // 2 - self.font.size("Уровень завершен! Нажмите Enter для продолжения")[0] // 2, self.height // 2)
            return

        self.draw_text(self.screen, level.title, self.width // 2 - self.font.size(level.title)[0] // 2, 20)
        self.draw_text(self.screen, self.clicked_letters, self.width // 2 - self.font.size(self.clicked_letters)[0] // 2, self.height // 2)

        self.draw_text(self.screen, f"Клики: {self.click_count}",
                       self.width // 2 - self.font.size(f"Клики: {self.click_count}")[0] // 2, self.height - 50)

    def draw_menu(self):
        self.screen.fill(self.WHITE)
        self.draw_text(self.screen, "Выберите уровень:", self.width // 2 - self.font.size("Выберите уровень:")[0] // 2,
                       self.height // 4)
        for i, level in enumerate(self.levels):
            self.draw_text(self.screen, f"{i + 1}. {level.title}",
                           self.width // 2 - self.font.size(f"{i + 1}. {level.title}")[0] // 2,
                           self.height // 4 + (i + 1) * 40)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if self.in_menu:
                try:
                    level_index = int(event.unicode) - 1
                    if 0 <= level_index < len(self.levels):
                        self.current_level = level_index
                        self.clicked_letters = ""
                        self.in_menu = False
                except ValueError:
                    pass  # ignore non-numeric input
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            else:
                if event.key == pygame.K_ESCAPE:
                    self.in_menu = True
                    self.clicked_letters = ""
                    self.click_count = 0
                elif event.key == pygame.K_SPACE:
                    level = self.levels[self.current_level]
                    if len(level.solution) > len(self.clicked_letters):
                        self.clicked_letters += level.solution[len(self.clicked_letters)]
                        self.click_count += 1
                elif event.key == pygame.K_RETURN and len(self.levels[self.current_level].solution) <= len(
                        self.clicked_letters):
                    self.current_level += 1
                    self.clicked_letters = ""
                    self.click_count = 0
                    if self.current_level >= len(self.levels):
                        self.in_menu = True
                        self.current_level = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_input(event)

            if self.in_menu:
                self.draw_menu()
            else:
                self.draw_level()

            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()