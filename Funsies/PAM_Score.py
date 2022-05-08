with open('PAM_Table.txt', 'r') as file:
    PAM_Table = [[int(float(element)) for element in num.split()] for num in file]

Strand1 = input('Enter Strand 1: ').replace(' ', '')
Strand2 = input('Enter Strand 2: ').replace(' ', '')

with open('Letters.txt', 'r') as file:
    letter_list = [letter.upper().replace('\n','') for letter in file]

sum = 0
for i in range(len(list(Strand1))):
    if list(Strand1)[i] == '-' or list(Strand2)[i] == '-':
        sum -= 5
    else:
        try:
            row = letter_list.index(list(Strand1)[i])
            col = letter_list.index(list(Strand2)[i])
            sum += PAM_Table[col][row]
        except:
            row = letter_list.index(list(Strand2)[i])
            col = letter_list.index(list(Strand1)[i])
            sum += PAM_Table[col][row]

print(f'PAM Score: {sum}')

