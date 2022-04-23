C = float(input('Enter Temperature in Celsius:'))
F = C*1.8 + 32
print('Temperature in Fahrenhiet:', F, 'F')
print('Weather Statement:')
if F >= 100:
    print('Warning: Heat Wave')
elif F >= 80 and F <= 99:
    print('Hot')
elif F >= 41 and F<= 79:
    print("Normal")
elif F >= 10 and F <= 40:
    print('Cold')
else:
    print('Input Temperature out of range, no weather statement available')











# def test(list):
#     Values = list
#     for numbers in Values:
#         print('Test Temperature in Celsius:', numbers, "C")
#         conversion(numbers)
#         print(' ')
# def conversion(a):
#     C = float(a)
#     F = C * 1.8 + 32
#     print('Temperature in Fahrenhiet:', F, 'F')
#     print('Weather Statement:')
#     if F >= 100:
#         print('Warning: Heat Wave')
#     elif F >= 80 and F <= 99:
#         print('Hot')
#     elif F >= 41 and F <= 79:
#         print("Normal")
#     elif F >= 10 and F <= 40:
#         print('Cold')
#     else:
#         print('Input Temperature out of range, no weather statement available')
#
# Test_Values = [-20,-10,0,10,20,30,40,50,60,70]
#
# test(Test_Values)
