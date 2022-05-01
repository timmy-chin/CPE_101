import unittest
from my_add import *


class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_add(1, 2), 3)
        self.assertEqual(my_add(2, 2), 4)
        self.assertEqual(my_add(3, 2), 5)
        self.assertEqual(my_add(4, 2), 6)

    def test_sub(self):
        self.assertEqual(my_sub(2,1),1)
        self.assertEqual(my_sub(3, 1), 2)
        self.assertEqual(my_sub(4, 1), 3)
        self.assertEqual(my_sub(5, 1), 4)
        self.assertEqual(my_sub(6, 1), 5)

    def test_compare(self):
        self.assertEqual(compare('Hello', 'Hello'), True)
        self.assertEqual(compare('Hello', 'Hello123'), False)
        self.assertEqual(compare('Hello', 'hello'), False)
        self.assertEqual(compare('Hello', 'hello123'), False)
        self.assertEqual(compare(type(1),type(2)), True)



#
if __name__ == '__main__':
    unittest.main()

# from my_add import *
#
# def test_add():
#     assert my_add(2,4) == 6, 'should be six'
#
# test_add()
# print('all ok')
#
# def test_sub():
#     assert my_sub(2,1) == 1, 'should be one'
#
# test_sub()
#
# def test_compare():
#     assert compare('hello','hello123') == False, 'should be False'
#     assert compare('Hello', 'hello') == False, 'should be False'
#     assert compare('Hello', 'Hello') == True, 'should be True'
#
# test_compare()
# print('Test Compare Passed')