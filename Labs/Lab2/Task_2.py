import random
def random_letters(name):
    name = name.replace(" ", "")
    name = name.lower()
    email = ''
    for i in range(5):
        ran_num = random.randint(0, len(name)-1)
        email += name[ran_num]
    email += "@calpoly.edu"
    return email

x = True
while x:
    name = input('Enter your name:')
    print(random_letters(name))











