string = input('5 letter string:')
if len(string) == 5:
    reverse_str = ''
    for i in range(5):
        reverse_str += string[4-i]
    print(reverse_str)
    if string == reverse_str:
        print(string, 'is a palindrome')
    else:
        print(string, 'is not a palindrome')
else:
    print('You must enter a 5 letter string')
