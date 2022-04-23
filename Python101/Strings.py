string = '''Hello Bro
This is so cool
Woah I can type so many lines'''
print(string)
string2 = 'Hello' \
          'Bro'
print(string2)

print('Hello I really can\'t Broooo')

string3 = 'Hello Hello\nGoodbye\nHello    Hello'
print(string3.rstrip())

#Exercise

my_string = 'This is a string of words'
print(my_string.split()[1])
print(my_string.replace(' ',''))

#String Formating

name = 'Timmy'
age = 5

print('My name is %s' % name, 'age %s' % age)


age = 18
name = 'Timmy'
print('Hello {} your age is {}'.format(name, age))
