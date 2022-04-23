def check_word(word):
    global list2
    i = 0
    for element in list2:
        if word == element:
            i += 1
            list2.remove(word)
    if i == 0:
        pass
    else:
        print(f'{word} = {i}')

def check_letter(letter):
    global str2
    i = 0
    for element in list(str2.upper()):
        if letter == element:
            i += 1
    print(f"{letter} = {i}")

def check_repeat(letter):
    global letterNoRepeat
    if not(letter in letterNoRepeat):
        letterNoRepeat += letter


str1 = input('Enter String 1: ')
str2 = input('Enter String 2: ')
list1 = str1.upper().split()
list2 = str2.upper().split()
letterToCheck = ''
letterNoRepeat = ''

for word in list1:
    check_word(word)

for letter in ''.join(list2):
    check_repeat(letter)

for letter in letterNoRepeat:
    check_letter(letter)

