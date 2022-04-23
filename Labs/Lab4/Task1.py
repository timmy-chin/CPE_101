sentence = input('Enter a Sentence: ')
three_words = False
while not three_words:
    if len(sentence.split()) < 3:
        print('Sentence Must be at least 3 words!')
        sentence = input('Enter Sentence: ')
    else:
        three_words = True

list_word = sentence.split()
modified_sentence = ''
for word in list_word:
    if 'o' in word.lower():
        print(word.upper(), end=' ')
    else:
        print(word, end=' ')

longest = list_word[0]
for word in list_word:
    if len(longest) < len(word):
        longest = word

print('\nLongest Word:', longest)
print('Length: ', len(longest))




