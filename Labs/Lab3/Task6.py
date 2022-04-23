import random

def collect_name():
    return input('Enter Name: ')

def email_generator(name):
    name = name.replace(' ', '')
    new_ID = ''
    for i in range(5):
        num = random.randint(0,len(name)-1)
        new_ID += name.lower()[num]
    return new_ID + '@calpoly.edu'

def print_email(email_ID):
    print(email_ID)

x= True
while x:
    name = collect_name()
    email_ID = email_generator(name)
    print_email(email_ID)