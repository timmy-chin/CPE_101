# import unittest
#
# def my_add(num1,num2):
#     return num1+num2
#
# class Test(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(my_add(1,2),3)
#
#
#
# if __name__ == '__main__':
#     unittest.main()


listA = [1,2,3,4,5]
listB = [5,6,7,8,9]

list3 = listA + listB

print(list3)

listA.extend(listB)
print(listA)

listB += listA

print(listB)

