import unittest
import game2

class CountCowsAndBullsTest(unittest.TestCase):

    def test_count_bulls(self):

        self.assertIsInstance(game2.count_bulls([1, 2, 3], [2, 5, 3]), int)
        self.assertEqual(game2.count_bulls([1,2,3], [2,5,3]), 1)
        self.assertEqual(game2.count_bulls([1, 2, 3, 9, 2, 3], [2, 5, 3, 3, 2, 9 ]), 2)

    def test_count_cows(self):
        self.assertIsInstance(game2.count_cows([1,2,3], [2,5,3]), int)




if __name__ == '__main__':
    unittest.main()
