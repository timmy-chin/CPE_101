# Array: a collection of similar or homogeneous data elements
# List: a collection of dissimilar or heterogeneous data elements

x = [[1,2,3],['a', 'b', 9]]
y = [10,2,34,100]

#accessing is similar to string slicing
print(y[1:3])
print(y[::])
print(y[1:])
print(len(y))

#Loops

for i in range(len(y)):
    print(y[i])
for i in range(5):
    print(i)

for num in range(500):
    print('I must not Lie')



