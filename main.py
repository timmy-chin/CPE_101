# def id(thing):
#     print(thing)
#
# x = 10
# course_name = 'CPE 101'
# y = x
# z = 10
#
# if x == course_name:
#     print('1. yes')
# elif not(x == course_name):
#     print('1. no')
#
#
# if x == y == z:
#     print('2. yes')
# elif not(x == y == z):
#     print('2. no')



#     if c == a//b:
#         print(a,"//", b)
#         print("TRUE")
#         print(c, '=', a//b)
#         print(' ')
#     else:
#         print('False')
#
# for i in range(10):
#     for j in range(200):
#         floordivision(float(j-100),i+2)

#
# x = "10.5"
#
# if str(float(x)) == x:
#     print('It is a float')
# else:
#     print('It is an integer')


#Using Comparison for Floor Division:
# a = input('a')
# b = input('b')
# if str(float(a)) == a:
#     print("A is a float")
#     a = float(a)
# else:
#     print('A is an integer')
#     a = int(a)
# if str(float(b)) == b:
#     print('B is a float')
#     b = float(b)
# else:
#     print('B is an integer')
#     b = int(b)
#
# c = a/b
# if c < 0 and a%b !=0:
#     c =int(c) - 1
# c = int(c)
#
# if type(a) == float or type(b) == float:
#     float(c)
#
# print('Floor Division by Function:', c)
#
#
# #Inputs for floordivison function
# a = input('Numerator:')
# b = input('Denominator:')
# if str(float(a)) == a:
#     a = float(a)
# else:
#     a = int(a)
# if str(float(b)) == b:
#     b = float(b)
# else:
#     b = int(b)
#
# floordivision(a,b)

# string = input('Type a Sentence:')
# vowels = 'aeiou'
#
# new_string = ''
# for i in range(len(string)):
#     Vowel = False
#     for j in range(len(vowels)):
#         if string[i-1].lower() == vowels[j-1]:
#             new_string += '%'
#             Vowel = True
#     if Vowel == False:
#         new_string += string[i-1]
# print(new_string)

#
# x = 10
# print(id(x))
# x = 20
# print(id(x))
# y = 10
# print(id(y))
# y = 20
# print(id(y))
# print('Apple'< 'apple')

# def arithmetic_mean(num1,num2):
#
#     a = num1
#     b = num2
#     print("inside function ids:", id(a), id(b))
#     sum = a+b
#     return int(sum / 2)
#
# import statistics
#
# a = 5
# b = 5
# print("outside function ids:", id(a), id(b))
# my_mean = arithmetic_mean(a,b)
# print(" Result of function computation", my_mean)
# data = [a,b]
# ans = statistics.mean(data)
# print(ans)
#
# def hello(s,n):
#     greeting = 'Good {} '.format(s+ ' '+str(n))
#     print(greeting*n)
#
# def bye(s,n):
#     greeting = 'Good '+ s
#     print(greeting*n)
#
# hello('Morning', 10)
# bye('Byebye ', 10)
#
# b = bye
#
# b('Hello', 10)


#
# def add(a, b):
#     return a + b
#
# def call_function(func, a, b):
#     print(func.__name__)
#     return func(a,b)
#
# call_function(add, 1,10)
#
# def add(x):
#     x = x + 1
#     print(x)
#
# x = 99
# add(x)
# print(x)

#
# def fun(name, unit):
#     print(f'This is the name: {name}, and this is the {unit}')
#
# fun('PM_25', 'umg')

# str = 'Hello'
# print(str[-1:1])
#
#
# def add(x):
#     return x + 1
#
#
# print(add(3))
# x = add(3)
# print(x)
#
# x = 10
# y = 10
# z = 10.0
# print(id(x), id(y), id(z))

# import random
# x = True
# while x:
#     ran_num = random.randint(0,2)
#     my_move = input('Enter your Move:').lower()
#     if ran_num == 0:
#         enemy_move = 'scissors'
#     elif ran_num == 1:
#         enemy_move = 'paper'
#     else:
#         enemy_move = 'rock'
#     print('Enemy Move:', enemy_move)
#
#     if my_move == enemy_move:
#         print('Tie')
#     elif my_move == 'scissors' and enemy_move == 'paper':
#         print('You Win')
#     elif my_move == 'paper' and enemy_move == 'rock':
#         print('You Win')
#     elif my_move == 'rock' and enemy_move == 'scissors':
#         print('You Win')
#     elif my_move == 'paper' and enemy_move == 'scissors':
#         print('You Lose')
#     elif my_move == 'rock' and enemy_move == 'paper':
#         print('You Lose')
#     elif my_move == 'scissors' and enemy_move == 'rock':
#         print('You Lose')
#     else:
#         print('Invalid Move')
#
# def subtract():
#     print('Hi')
# def add(func):
#     '''This Function does nothing'''
#     print(func.__name__)
#     func()
#
#
# print(add.__doc__)

# a = 'Python'
# b = a[4:]
#
# if b == 'on':
#     print(a, " is a programming language")
#
# else:
#     print(a,"is a snake")
#
# for x in 'string':
#     print(x)

# def check_valid(i, result):
#     if int(str(result)[1]) == int(str(i)[0]) + int(str(i)[1]):
#         return True
#     else:
#         return False
# count = 10
# while count < 99:
#     result = count * 11
#     print('Count: ', count)
#     print(check_valid(count, result))
#     count += 1


# print('hello\nhello')
#
# ans = 5
#
# if ans in range(0,10):
#     print(ans)


# while True:
#     print('Hi')
#     break
#
# list = ['My friend', 'Celine', 'Timmy']
# string = 'Hello'
#
# for i, people in enumerate(string):
#     print(i)
#     print(people)


# x = True
# while x:
#     print('Hi')
#     print('Hi')
#     x = False
#     print('Do you still run what is after x = False???')
#
# print(list(range(5)))
#
# a = 'Python'
# b = a[4:]
#
# if b == 'on':
#     print(a, ' is a programming language')
# else:
#     print(a,'is a snake')

# str = 'Hello this world is trash'
#
# print(list(str))
#
# n = '6'
# print(n.isdigit())

import math

# a = [1,2,3,4,4]
# a.insert(10, 2)
# print(a)
# a.remove(2)
# print(a)
# a.pop(3)
# print(a)
#
# print('Ayo I am making some changes to the main file in python, will Github show the changes???')
#
# print('Wow this is so cool!!!')

# print((5 < 10))
#
# my_list = [1,2,3,4]
# new_list = my_list.copy()
# my_list.append(5)
#
# print(new_list)
# print(my_list)

# list = [1,2,3,4,5]
# list[0] = 10
# print(list)

# vector_dict = dict()
# angle_dict = dict()
#
# n = int(input('Enter Number of Vectors: '))
#
# i = 0
# while i < n:
#     i+= 1
#     vector_dict[f"Vector{i}"] = float(input(f'|V{i}| = '))
#     angle_dict[f"Angle{i}"] = float(input(f'V{i} Angle: '))
#
# print(vector_dict)
# print(angle_dict)
#
# print(vector_dict['Vector2'])

list1 = [1,2,3,4,5,3,3,3,3]
set = list(set(list1))
print(set)