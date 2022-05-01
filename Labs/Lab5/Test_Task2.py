import unittest
import Task2

class testTask2(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(Task2.calculate_average([1,2,3,4,5]),3)
        self.assertEqual(Task2.calculate_average([6,7,8,9,10]), 8)
