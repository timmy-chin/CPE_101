import time
from Password import Password

def hack_password(Password):
    for num in range(int(Password)+1):
        num_of_zero = len(Password) - len(str(num))
        password_str = ''
        for i in range(num_of_zero):
            password_str += '0'
        password_str += str(num)
        if password_str == Password:
            return Password


print('Welcome to Facebook\n\nEnter Email: timmychin123@hotmail.com\n\n')
start_time = time.time()
Pass = False
while not Pass:
    password = hack_password(Password)
    if password == Password:
        print('Logged In')
        Pass = True
    else:
        print('Wrong Password, Try Again!')



print('')
print(f'Password is {password}')
print(f'Time it Took to Crack Password: {time.time() - start_time} seconds')



