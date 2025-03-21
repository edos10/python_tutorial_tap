import unittest
import json
import os
from internal.draw import Game


class TestGameIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('levels.json', 'w', encoding='utf-8') as f:
            json.dump({"levels": [1, 2, 3]}, f)

        with open('clicks.txt', 'w') as f:
            f.write('15')

        with open('levels.txt', 'w') as f:
            f.write('1\n2\n3\n')

    @classmethod
    def tearDownClass(cls):
        os.remove('levels.json')
        os.remove('clicks.txt')
        os.remove('levels.txt')

    def test_init(self):
        game = Game(font=None, path_levels='levels.json')

        # Проверяем, что уровни загружены правильно
        self.assertEqual(game.levels, {"levels": [1, 2, 3]})
        self.assertEqual(game.clicks, 15)
        self.assertEqual(game.levels_done, [1, 2, 3])

    def test_load_completed_levels(self):
        game = Game(font=None, path_levels='levels.json')
        game.load_completed_levels()
        self.assertEqual(game.levels_done, [1, 2, 3])

    def test_is_done_level_completed(self):
        game = Game(font=None, path_levels='levels.json')
        game.load_completed_levels()

        # Проверяем, что уровень 1 считается завершенным (уровень 2 завершен)
        self.assertTrue(game.is_done_level(1))

    def test_is_done_level_edge_case(self):
        game = Game(font=None, path_levels='levels.json')
        game.load_completed_levels()

        # Проверяем уровень 3 (последний) - он не должен быть завершен
        self.assertFalse(game.is_done_level(3))

    def test_is_done_level_non_existent(self):
        game = Game(font=None, path_levels='levels.json')
        game.load_completed_levels()

        # Проверяем уровень 0 (не существует) - он не должен быть завершен
        self.assertFalse(game.is_done_level(4))

    def test_load_empty_completed_levels(self):
        # Создаем пустой levels.txt для теста
        with open('levels.txt', 'w') as f:
            f.write('')

        game = Game(font=None, path_levels='levels.json')
        game.load_completed_levels()

        # Проверяем, что levels_done пустой
        self.assertEqual(game.levels_done, [])

    def test_load_nonexistent_file(self):
        # Проверяем обработку отсутствующего файла levels.json
        with self.assertRaises(FileNotFoundError):
            game = Game(font=None, path_levels='nonexistent_levels.json')

    def test_invalid_clicks_format(self):
        # Проверяем обработку некорректного формата clicks.txt
        with open('clicks.txt', 'w') as f:
            f.write('invalid_number')

        game = Game(font=None, path_levels='levels.json')

        self.assertEqual(game.clicks, 0)


if __name__ == '__main__':
    unittest.main()
