transcription = False
choice = input('DNA or RNA: ')
if choice == 'DNA':
    strand = input('Enter DNA strand: ')
    strand = strand.replace(' ', '')
    transcription = True
elif choice == 'RNA':
    RNA_strand = input('Enter RNA strand: ')
    RNA_strand = RNA_strand.replace(' ', '')

if transcription:
    RNA_strand = []
    for letter in strand:
        if letter == 'G':
            RNA_strand.append('C')
        elif letter == 'C':
            RNA_strand.append('G')
        elif letter == 'A':
            RNA_strand.append('U')
        elif letter == 'T':
            RNA_strand.append('A')

Start = False
translation = []
First = 0
Second = 0
Third = 0
count = 0
code = ''
for letter in RNA_strand:               #Creating List with Between AUG start and Stop UAC, UAA, UGA
    First = Second
    Second = Third
    Third = letter
    if f'{First}{Second}{Third}' == 'AUG':
        Start = True

    if Start:
        code += First
        count += 1
        if code == 'UAG' or code == 'UAA' or code == 'UGA':
            Start = False
            break
        if count == 3:
            translation.append(code)
            count = 0
            code = ''
if Start:
    code += Second
    translation.append(code)

code_list = []
protein_list = []
count = 0

for one in ['U', 'C', 'A','G']:                 #Creating Code List with its index corresponding to another list named protein_list
    for two in ['U', 'C', 'A', 'G']:
        for three in ['U', 'C', 'A', 'G']:
            letter_str = f'{one}{two}{three}'
            code_list.append(letter_str)
            count += 1
            if count <= 2:
                protein_list.append('F')
            elif count <= 4:
                protein_list.append('L')
            elif count <= 8:
                protein_list.append('S')
            elif count <= 10:
                protein_list.append('Y')
            elif count <= 12:
                protein_list.append('Stop')
            elif count <= 14:
                protein_list.append('C')
            elif count <= 15:
                protein_list.append('Stop')
            elif count <= 16:
                protein_list.append('W')
            elif count <= 20:
                protein_list.append('L')
            elif count <= 24:
                protein_list.append('P')
            elif count <= 26:
                protein_list.append('H')
            elif count <= 28:
                protein_list.append('Q')
            elif count <= 32:
                protein_list.append('R')
            elif count <= 35:
                protein_list.append('I')
            elif count <= 36:
                protein_list.append('M')
            elif count <= 40:
                protein_list.append('T')
            elif count <= 42:
                protein_list.append('N')
            elif count <= 44:
                protein_list.append('K')
            elif count <= 46:
                protein_list.append('S')
            elif count <= 48:
                protein_list.append('R')
            elif count <= 52:
                protein_list.append('V')
            elif count <= 56:
                protein_list.append('A')
            elif count <= 58:
                protein_list.append('D')
            elif count <= 60:
                protein_list.append('E')
            elif count <= 64:
                protein_list.append('G')

protein = []
for code in translation:                #Taking index of code and finding protein translation with that index in the protein_list, like using a directory
    try:
        index = code_list.index(code)
        protein.append(protein_list[index])
    except:
        code += Third
        translation.pop(-1)
        translation.append(code)
        index = code_list.index(code)
        protein.append(protein_list[index])

if transcription:
    print('DNA: ', end="")
    for letter in strand:
        print(letter, end='')
    print()

print('RNA: ', end="")
for letter in RNA_strand:
    print(letter, end='')
print()

print(f'Code to Translate: {translation}')

print('Translation: ', end="")
for letter in protein:
    print(letter, end='')
print('\n')



