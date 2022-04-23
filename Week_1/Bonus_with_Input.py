def floordivision(a,b):
    c = a/b
    if c < 0 and a%b != 0:
        c = int(c) - 1
    c = int(c)
    if type(a) == float or type(b) == float:
        c = float(c)
    print('Floor Division with my Function:', c)
    print('Floor Division with Operator:', a//b)
    print('Input Type: a:', type(a), 'b:', type(b))
    print('Output Type:', type(c))

a = input('Numerator:')
b = input('Denominator:')
if str(float(a)) == a:
    a = float(a)
else:
    a = int(a)
if str(float(b)) == b:
    b = float(b)
else:
    b = int(b)

floordivision(a,b)
