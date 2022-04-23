def replace_char(char):
    if ord('a') <= ord(char) <= ord('m') or ord('A') <= ord(char) <= ord('M'):
        new_index = ord(char) + 13
        return chr(new_index)
    elif ord('n') <= ord(char) <= ord('z') or ord('N') <= ord(char) <= ord('Z'):
        new_index = ord(char) - 13
        return chr(new_index)
    elif not(char.isalpha()):
        return char


print(replace_char(input('Enter a Character: ')))




