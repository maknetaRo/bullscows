import unittest
import game

class CountCowsAndBullsTest(unittest.TestCase):

    def test_random_numbers(self):
        self.assertNotEqual(game.random_numbers(), 0)

        self.assertListEqual(game.random_numbers(), [1, 2, 3, 4])

    def test_count_cows(self):
        self.assertEqual(game.count_cows([1, 2, 3, 4], [4, 5, 6, 7]), 1)
        self.assertEqual(game.count_cows([1, 2, 3, 4], [4, 5, 6, 2]), 2)
        self.assertEqual(game.count_cows([1, 2, 3, 4], [9, 0, 3, 8]), 1)
        self.assertEqual(game.count_cows([1, 2, 3, 4], [9, 5, 6, 7]), 0)

    def test_count_bulls(self):
        self.assertEqual(game.count_bulls([1, 2, 3, 4], [1, 2, 5, 6]), 2)
        self.assertEqual(game.count_bulls([1, 2, 3, 4], [1, 0, 5, 6]), 1)
        self.assertEqual(game.count_bulls([1, 2, 3, 4], [2, 0, 5, 6]), 0)

if __name__ == '__main__':
    unittest.main()
