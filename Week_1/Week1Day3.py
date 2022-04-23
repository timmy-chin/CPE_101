a = 'Programming CPE 101'
print('Access all characters:',a[:])
print('Access gram:', a[3:7])
ch1 = a[3:]
print('Access all elements from index 3:', ch1)
print(a[2:30])
#print(a[30])

print('Reverse index access 101:', a[-3:])

b = 'Hello'
print("Access el using reverse indexing:", b[-4:-2])

list = [1,2,3,4,5]

print(len(b))
#prints length of the character


x = " "
y = ''
print(round(2.51))

#Bonus question: How to code floor division without using // and without using round, ceiling. You can only use operators

print('Apple' == 'Apple')
print('Apple' < 'apple')
print("Apple" < "Apple123")
print('zzple123' < 'zpple123')

a = 20
b = "Hello"
print(a,b)
#Cannot use plus because it is only for string data type
c = str(a)
print(c + b)
#for plus, there is no space in between the two variable, to add space, do this
print(c +' '+ b)