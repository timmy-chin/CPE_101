class STD:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __lt__(self, other):
        return self.mark < other.mark

    def __gt__(self, other):
        return self.mark > other.mark

    def __repr__(self):
        return self.mark

n = int(input('Enter Number of Students: '))
students = [STD(input(f'Student {i+1} Name: '), input(f'Student {i+1} Mark: ')) for i in range(n)]

student1 = students[0]
max = student1

for index, student in enumerate(students):
    if student > max:
        max = student
        num = index

maxstudent = students[num]
print(f'\nStudent Name with Max: {maxstudent.name}')
print(f'Student Max Score: {maxstudent}')
