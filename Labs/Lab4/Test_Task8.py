import unittest
import Task8

class TestTask8(unittest.TestCase):
    def test_less_than_5(self):
        self.assertEqual(Task8.less_than_5(['Python', 'Ava', "Shakespear", 'Java']), 2)
        self.assertEqual(Task8.less_than_5(['Timmy', 'Celine', 'Anthony', 'Tasha', 'Jesus', 'Joe', "Jack", 'Zach']), 3)

if __name__ == '__main__':
    unittest.main()