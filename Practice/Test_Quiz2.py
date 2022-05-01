import unittest
import Quiz2

class testQuiz2(unittest.TestCase):
    def test_summation(self):
        self.assertEqual(Quiz2.summation(2,8,2),12)
        self.assertEqual(Quiz2.summation(3,14,3),30)

    def test_max_index(self):
        self.assertEqual(Quiz2.max_index([10,12,13]),3)
        self.assertEqual(Quiz2.max_index([10,15,20,10,5,7,100]), 7)
        self.assertEqual(Quiz2.max_index([1000,10,20,30]), 1)


if __name__ == '__main__':
    unittest.main()