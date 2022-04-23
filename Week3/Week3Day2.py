def change_x():
    x = 1
    print('x inside the function:', x)

def my_avg():
    a = res/3
    print('Avg is:', a)

def my_add(p,q):
    z = int(input('Give number for z'))
    res = p+q+z
    print(res)
    return res

x = 10
change_x()

print('x value outside function:', x)

res = my_add(1,2)
print('Result of add:', res)
my_avg()

print(my_add(1,2))

#Literally, return is just a content that is spit out from a function and it should contained in a variable or put into a function for use, don't just leave it hanging out in space
