def summation(start, stop, steps):
    add = start
    sum = start
    while True:
        add += steps
        if add < stop:
            sum += add
        else:
            break
    return sum

def max_index(list_num):
    max = list_num[0]
    index = 0
    for x in list_num:
        if max < x:
            max = x
    for i in range(len(list_num)):
        if list_num[i] == max:
            return i + 1


