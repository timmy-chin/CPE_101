def checkvalid(x):
    global num1, num2, num3
    if x < 100:
        num1 = int(str(x)[0] + '0')
        num2 = int(str(x)[0])
        num3 = int(str(x)[1])
    elif x < 1000:
        num1 = int(str(x)[0] + '00')
        num2 = int(str(x)[0:2])
        num3 = int(str(x)[1:3])
    print(f"{x} * 11 = {x * 11}")
    print(f"{num1}+ ({num2}+{num3}) = {num1 + (num2 + num3)}")
    if str(x * 11) == str(num1 + (num2 + num3)) + str(x)[-1]:
        return True
    else:
        return False

for x in range(10,1000):
    print(checkvalid(x),'\n')


