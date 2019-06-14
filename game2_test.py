import unittest
import game2

class CountCowsAndBullsTest(unittest.TestCase):

    def test_count_bulls(self):

        self.assertIsInstance(game2.count_bulls([1, 2, 3], [2, 5, 3]), int)
        self.assertEqual(game2.count_bulls([1,2,3], [2,5,3]), 1)
        self.assertEqual(game2.count_bulls([1, 2, 3, 9, 2, 3], [2, 5, 3, 3, 2, 9 ]), 2)

    def test_count_cows(self):
        self.assertIsInstance(game2.count_cows([1,2,3], [2,5,3]), int)
        self.assertEqual(game2.count_cows([1,2,3], [2,5,3]), 1)
        self.assertEqual(game2.count_cows([1, 2, 3, 9, 2, 3], [2, 5, 3, 3, 2, 9 ]), 3)

    def test_random_numbers(self):
        self.assertIsInstance(game2.random_numbers(), list)

    def test_random_letters(self):
        self.assertIsInstance(game2.random_letters(), list)

    def test_play_game(self):
        self.assertTrue(game2.play_game())
        self.assertIsInstance(game2.play_game(), list)
    #     self.assertEqual(game2.play_game(), "Bulls: 0, cows: 0.")
    #     self.assertEqual(game2.play_game([1,2,3], [4,5,6]), "Bulls: 0, cows: 0.")



if __name__ == '__main__':
    unittest.main()
