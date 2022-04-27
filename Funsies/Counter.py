
word_list = []
with open('Chat.txt', 'r') as file:
    for word in file:
        word = word.replace('\n', '')
        word_list.append(word)
print(word_list)

Start_Count = False

for word in word_list:
    if 'Terence' in word_list:
        word_list.remove('Terence')

i = 0
for word in word_list:
    if word[0:7] == 'Terence':
        Start_Count = True
    if word[0:3] == 'You' or word[0:1].isdigit():
        Start_Count = False
    if Start_Count:
        i += 1

print(f'Total Messages: {i}')

