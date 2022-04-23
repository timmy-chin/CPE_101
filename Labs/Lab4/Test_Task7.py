import unittest
import Task7

class TestTask7(unittest.TestCase):
    def test_middle(self):
        self.assertEqual(Task7.middle([1,2,3,4]),[2,3])
        self.assertEqual(Task7.middle([5,7,9,11,14,16]),[7,9,11,14])

if __name__ == '__main__':
    unittest.main()