list_num = []
list_den = [2,3,4,0,5,6,8]
while len(list_num) != len(list_den):
    num = int(input('Enter Number: '))
    while num < 10:
        print('Number must be greater than or equal to 10')
        num = int(input('Enter Number: '))
    list_num.append(num)

result = []

for i in range(len(list_den)):
    if list_den[i] == 0:
        division = -1
    else:
        division = list_num[i] / list_den[i]
    result.append(division)

print('Results:', result)
