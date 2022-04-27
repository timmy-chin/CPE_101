def replace_char(char):
    if ord('a') <= ord(char) <= ord('m') or ord('A') <= ord(char) <= ord('M'):
        integer = ord(char) + 13
        return chr(integer)
    elif ord('n') <= ord(char) <= ord('z') or ord('N') <= ord(char) <= ord('Z'):
        integer = ord(char) - 13
        return chr(integer)
    elif not(char.isalpha()):
        return char


print(replace_char(input('Enter a Character: ')))




