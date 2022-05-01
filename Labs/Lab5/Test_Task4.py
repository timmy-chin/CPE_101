import unittest
import Task4
import math

class testTask4(unittest.TestCase):
    def test_my_exp(self):
        self.assertEqual(Task4.my_exp(5),round(math.e ** 5,3))
        self.assertEqual(Task4.my_exp(7), round(math.e ** 7,3))

if __name__ == '__main__':
    unittest.main()
