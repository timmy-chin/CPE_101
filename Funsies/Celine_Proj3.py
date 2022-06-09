class Employee:
    def __init__(self, name, age,position):
        self.name = name
        self.age = age
        self.position = position

employee_info = [('Michael', '45', 'Manager'), ('Dwight', '40', 'Assistant to the Manager'), ('Jim', '35', 'Manager'), ('Pam', '30', 'Receptionist'),
                 ('Angela', '32', 'Accountant'), ('Kevin', '42', 'Accountant'), ('Oscar', '40', 'Accountant'), ('Stanley', '55', 'Salesperson'),
                 ('Phyllis', '45', 'Salesperson'), ('Andy', '38', 'Salesperson'), ('Ryan', '30', 'Salesperson'), ('Creed', '55', 'Salesperson')]
employee_list = [Employee(name, age, position) for name, age, position in employee_info]

