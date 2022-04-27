# list = [20,10,1,2,3,4,5,6]
# list.pop(10)
# print(list)

file = open('Open.txt','r')
string = file.read()
list = string.split('\n')
write_file = open('write.txt', 'w')

print(write_file.writable())

for element in list:
    write_file.write(element)
    write_file.write('\n')
