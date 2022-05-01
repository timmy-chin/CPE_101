def calculate_average(list):
    sum = 0
    for x in list:
        sum += x
    mark.sort()
    return sum / 5

mark = []
for i in range(5):
    mark.append(int(input(f'Enter Mark for Student {i+1}: ')))



print(f'Average Marks: {calculate_average(mark)}')
print(f'Marks in Ascending Order: {mark}')