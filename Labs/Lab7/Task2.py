class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}: {self.age}'

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

def insertion_sort():
    global list_employee
    count = 0
    print(f'Pass 0: {list_employee}')
    for i in range(1, len(list_employee)):
        key = list_employee[i]
        current_index = i
        compare = list_employee[i-1]
        if not(compare < key):
            count += 1
            while i >= 0:
                i -= 1
                compare = list_employee[i]
                if compare > key:
                    pass
                else:
                    break
            new_index = i + 1
            list_employee.insert(new_index, key)
            list_employee.pop(current_index + 1)
            print(f'Pass {count}: {list_employee}')

def search(list):
    age = int(input('Enter Age: '))
    name = [employee.name for employee in list if employee.age == age]
    for emp_name in name:
        print(f'Name: {emp_name}')

info = [('Michael', 45), ('Jim', 35), ('Pam', 30), ('Dwight', 40), ('Creed', 60)]
list_employee = [employee(name, age) for name, age in info]

print('First Sorting:')
insertion_sort()

list_employee.append(employee('Toby', 45))
print('\nSecond Sorting:')
insertion_sort()
print('')

while True:
    search(list_employee)
