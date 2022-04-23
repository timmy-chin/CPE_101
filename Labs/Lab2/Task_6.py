def repeat():
    name = input('Enter your name:')
    first_letter = name[0]
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    green_light = False
    for i in range(len(valid_letters)):
        if first_letter.lower() == valid_letters[i - 1]:
            green_light = True
    if green_light == False:
        print('First Letter must be a letter')
        repeat()
    elif green_light == True:
        if first_letter.upper() == name[0]:
            print('The first letter of the name is in uppercase')
        else:
            new_name = name.capitalize()
            print(new_name)
name = input('Enter your name:')
first_letter = name[0]
valid_letters = 'abcdefghijklmnopqrstuvwxyz'
green_light = False
if first_letter.lower() in valid_letters:
    green_light = True
if not green_light:
    print('First Letter must be a letter')
    repeat()
else:
    if first_letter.upper() == name[0]:
        print('The first letter of the name is in uppercase')
    else:
        new_name = name.capitalize()
        print(new_name)


