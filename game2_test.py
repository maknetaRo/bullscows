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
    #
    # def test_random_elements(self):
    #     self.assertIsInstance(game2.random_elements(random_elements), list)

    # def test_get_input(self):
    #     #self.assertEqual(game2.get_input(), "Enter X numbers from 1 to 9.")
    #     self.assertIsInstance(game2.get_input(), list)

    def test_play_game(self):
        guess_secret = [1, 2, 3]
        self.assertEqual(game2.play_game(), "Bulls: 0, cows: 0.")
        self.assertEqual(game2.play_game(), "Bulls: 0, cows: 0.")



if __name__ == '__main__':
    unittest.main()
