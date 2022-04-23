import random
Give_up = True
memory_list = []
i = 0
while Give_up:
    a = random.randint(0,1)
    b = random.randint(0,1)
    c = random.randint(0,1)
    d = random.randint(0,1)
    memory_str = str(a) + str(b) + str(c) + str(d)
    green_light = True
    for memory in memory_list:
        if memory == memory_str and i == 40:
            Give_up = False
            green_light = False
        elif memory == memory_str:
            i+= 1
            green_light = False

    if green_light:
        i = 0
        memory_list.append(memory_str)
        print('A:', bool(a), 'B:', bool(b), 'C:', bool(c),'D:', bool(d))
        expression = (not(a or b or c or d) == (not a and not b and not c and not d))
        print('Expression is:', expression, '\n')

print(memory_list)


