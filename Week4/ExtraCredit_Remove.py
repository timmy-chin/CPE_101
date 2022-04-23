def my_remove(element):
    global listA
    while element in listA:
        listA.remove(element)

listA = []
n = int(input('List Size: '))
i = 0
while i <n:
    listA.append(input(f"Enter Element {i+1}: "))
    i+= 1

print('This is your list: \n', listA)

my_remove(input('Element to Remove: '))
print('This is your new list:\n', listA)

