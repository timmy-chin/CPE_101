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


class list:
    def __init__(self, list):
        self.list = list

    def __repr__(self):
        return str(self.list)

    def insertion_sort(self):
        count = 0
        print(f'Pass 0: {self.list}')
        for i in range(1, len(self.list)):
            key = self.list[i]
            current_index = i
            compare = self.list[i - 1]
            if not (compare < key):
                count += 1
                while i >= 0:
                    i -= 1
                    compare = self.list[i]
                    if compare > key:
                        pass
                    else:
                        break
                new_index = i + 1
                self.list.insert(new_index, key)
                self.list.pop(current_index + 1)
                print(f'Pass {count}: {self.list}')

    def append(self, element):
        self.list.append(element)


def search(list):
    age = int(input('Enter Age: '))
    name = [employee.name for employee in list if employee.age == age]
    for emp_name in name:
        print(f'Name: {emp_name}')


info = [('Michael', 45), ('Jim', 35), ('Pam', 30), ('Dwight', 40), ('Creed', 60)]
list_employee = list([employee(name, age) for name, age in info])

print('First Sorting:')
list_employee.insertion_sort()

list_employee.append(employee('Toby', 45))
print('\nSecond Sorting:')
list_employee.insertion_sort()
print('')

while True:
    search(list_employee.list)
