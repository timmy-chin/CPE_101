def is_palindrome(string):
    reverse_string = ''
    for i in range(len(string)):
        reverse_string += string[-(i+1)]
    if string == reverse_string:
        return True
    else:
        return False

def filter_palindrome(list):
    new_list = []
    for x in list:
        if is_palindrome(x):
            new_list.append(x)
    return new_list


n = int(input('Enter List Size: '))
listA = []
for i in range(n):
    listA.append(input('Enter a 5 letter String: '))

print(f'Your List: {listA}')
print(f'List with Palindromes: {filter_palindrome(listA)}')
