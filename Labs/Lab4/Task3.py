list_student = ['Ada Lovelace', 'Evelyn Boyd Granville', 'Geoffrey Hinton']
list_marks = [[79, 90, 89], [91,78,89], [81,82,89]]

for i in range(len(list_student)):
    name = list_student[i]
    three_marks = list_marks[i]
    total_mark = 0
    for marks in three_marks:
        total_mark += marks
    average_mark = total_mark / 3
    highest = three_marks[0]
    for mark in three_marks:
        if highest < mark:
            highest = mark
    print('Name: ', name)
    print('Average Grade: ', average_mark)
    print('Highest Grade: ', highest, '\n')

