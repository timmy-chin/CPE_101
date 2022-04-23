def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiple(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

def calculator():
    num1 = int(input('Enter First Integer Number:'))
    num2 = int(input('Enter Second Integer Number:'))
    operator = input('Enter Operator')
    if operator == '+':
        print(add(num1,num2))
    elif operator == '-':
        print(subtract(num1,num2))
    elif operator == '*':
        print(multiple(num1,num2))
    elif operator == '/':
        print(divide(num1, num2))
    else:
        print('Invalid Operator')

calculator()