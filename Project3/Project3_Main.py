class Employee:
    """A Class for Employees with name, age, position and department as attributes.
     Department has an empty string because it will be assigned in a function"""
    def __init__(self, name, age, position, department=''):
        self.name = name
        self.age = age
        self.position = position
        self.department = department


def display_employees(employee_list):
    """Print all employee attributes by assigning 'employee' as self for all
    employee objects in employee_list and printing them"""
    print('\nEmployees in Dunder Mifflin are:\n\n')
    for employee in employee_list:
        print(f'{employee.name},{employee.age},{employee.position}')


def allocation_department(employee_list):
    """Assign department to each employee object based on their position and appending employee
    objects into lists based on department and appending all 3 lists into a bigger list"""
    tuples = [('Manager','Management'), ('Salesperson','Sales'), ('Accountant','Accounts')]
    return [[Employee(employee.name, employee.age, employee.position, department) for employee in employee_list if position in employee.position] for position, department in tuples]


def display_department_employees(employee_department_list):
    """Print all employee object attributes under their specified department category"""
    print('\n\n\nThe individual employees in each department are shown below:\n--------------------------------------------------')
    for index, department in enumerate(['Management', 'Salespersons', 'Accountants']):
        print(f'\n\n{department}:')
        for employee in employee_department_list[index]:
            print(f'{employee.name},{employee.age},{employee.position}')


def head_of_department(employee_department_list):
    """Assign head position to employee objects with the highest age within their specified department"""
    for department in employee_department_list:
        max_age = max([employee.age for employee in department])
        for index, employee in enumerate(department):
            if employee.age == max_age:
                department[index] = Employee(employee.name, employee.age, f'Head {employee.position}', employee.department)


employee_info = [('Michael', '45', 'Manager'), ('Dwight', '40', 'Assistant to the Manager'), ('Jim', '35', 'Manager'), ('Pam', '30', 'Receptionist'),
                 ('Angela', '32', 'Accountant'), ('Kevin', '42', 'Accountant'), ('Oscar', '40', 'Accountant'), ('Stanley', '55', 'Salesperson'),
                 ('Phyllis', '45', 'Salesperson'), ('Andy', '38', 'Salesperson'), ('Ryan', '30', 'Salesperson'), ('Creed', '55', 'Salesperson')]

employee_list = [Employee(name, age, position) for name, age, position in employee_info]

display_employees(employee_list)

employee_list_department = allocation_department(employee_list)

display_department_employees(employee_list_department)

head_of_department(employee_list_department)

print('\n\n\n\n###############################\nHead of department allocation done!!!\n###############################\n')

display_department_employees(employee_list_department)