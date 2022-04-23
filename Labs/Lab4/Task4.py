n = int(input('Enter Non-negative Integer for Factorial: '))

while n < 0:
    print('Number must be Positive')
    n = int(input('Enter Non-negative Integer for Factorial: '))

j = 1
i = 1
while i <= n:
    j = j * i
    i += 1

print(f'{n}! = {j}')
