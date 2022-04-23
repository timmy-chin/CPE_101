import unittest
import Task6

class TestTask6(unittest.TestCase):
    def test_cumulative(self):
        self.assertEqual(Task6.cumulative([1,2,3]), [1,3,6])
        self.assertEqual(Task6.cumulative([2, 4, 6]), [2, 6, 12])

if __name__ == '__main__':
    unittest.main()
