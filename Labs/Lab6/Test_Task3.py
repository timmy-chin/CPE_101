import unittest
import Task3


class Test_Task3(unittest.TestCase):
    def test_groups_of_3(self):
        self.assertEqual(Task3.groups_of_3([1, 2, 3, 4, 5, 6]), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(Task3.groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]), [[1, 2, 3], [4, 5, 6], [7, 8]])


if __name__ == '__main__':
    unittest.main()
