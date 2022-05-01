import unittest
import Task1

class testTask1(unittest.TestCase):
    def test_chop(self):
        self.assertEqual(Task1.chop([1,2,3,4]),[1,4])
        self.assertEqual(Task1.chop([3,4,5,6]), [3,6])
