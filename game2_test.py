import unittest
import game2

class CountCowsAndBullsTest(unittest.TestCase):

    def test_count_bulls(self):
        
        self.assertIsInstance(game2.count_bulls([1, 2, 3], [2, 5, 3]), int)




if __name__ == '__main__':
    unittest.main()
