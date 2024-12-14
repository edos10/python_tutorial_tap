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
