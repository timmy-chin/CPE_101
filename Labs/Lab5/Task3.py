def is_palindrome(string):
    reverse_string = ''
    for i in range(len(string)):
        reverse_string += string[-(i+1)]
    return string == reverse_string

def filter_palindrome(list):
    return [x for x in list if is_palindrome(x)]

n = int(input('Enter List Size: '))
listA = [input('Enter a 5 letter String: ') for i in range(n)]

print(f'Your List: {listA}')
print(f'List with Palindromes: {filter_palindrome(listA)}')

