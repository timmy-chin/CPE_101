import random

name_list = ["Ada Lovelace", 'Grace Hopper', 'Barbara Liskov','Timmy Chin', 'Celine Ha', 'Anthony Man']
list_A = []
for name in name_list:
    name = name.replace(' ','')
    name = name.lower()
    list_A.append(name)

email_list = []
for i in range(len(list_A)):
    random_name = ''
    name = list_A[i]
    for i in range(5):
        num = random.randint(0,len(name)-1)
        random_name += name[num]
    random_name += '@calpoly.edu'
    email_list.append(random_name)

for name in email_list:
    print(name)

