def factorial(i):
    factorial = 1
    for n in range(i):
        factorial *= (n+1)
    return factorial

def my_exp(x):
    result = 1
    for i in range(1,100):
        Numerator = x**i
        Denominator = factorial(i)
        result += (Numerator/Denominator)
    return round(result,3)

