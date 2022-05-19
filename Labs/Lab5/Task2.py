def calculate_average(list):
    sum = 0
    for x in list:
        sum += x
    return sum / 5

if __name__ == '__main__':

    mark = [int(input(f'Enter Mark for Student {i+1}: ')) for i in range(5)]

    print(f'Average Marks: {calculate_average(mark)}')
    mark.sort()
    print(f'Marks in Ascending Order: {mark}')