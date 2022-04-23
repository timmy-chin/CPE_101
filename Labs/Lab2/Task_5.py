x1 = input('x1:')
y1 = input('y1:')
x2 = input('x2:')
y2 = input('y2:')

distance = ((float(x2) - float(x1))**2+(float(y2) - float(y1))**2)**0.5

print('Distance between ('+ x1+','+y1+') and ('+x2+','+y2+') is:', distance)
