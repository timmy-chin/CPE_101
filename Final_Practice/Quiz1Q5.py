def odd_even(num):
    sign = 'Negative'
    if num > 0:
        sign = 'Positive'
    type = 'Odd'
    if num % 2 == 0:
        type = 'Even'
    print(f'Number is {sign} and {type}')

def transaction(list_num):
    sum = 0
    total = 0
    for num in list_num:
        if num > 0:
            sum += num
            total += 1
    return sum / total

def max_of_3(list_num):
    max = list_num[0]
    for num in list_num:
        if num > max:
            max = num
    return max

def sum_nums(start, stop, step):
    sum = start
    add = start
    while True:
        print(add)
        add += step
        if add < stop:
            sum += add
        else:
            break
    return sum


def be_positive(list_num):
    new_list = []
    for num in list_num:
        if num >= 0:
            pass
        else:
            num = abs(num)
        new_list.append(num)
    return new_list

def booking_movie_tickets(list_num):
    movie_list = []
    for num in list_num:
        if even(num):
            movie_list.append('Star Trek')
        else:
            movie_list.append('Toy Story')
    return movie_list

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def rental_late_fee(list_num):
    zero = False
    week = False
    month = False
    for num in list_num:
        if num > 30:
            month = True
            break
        elif num == 0:
            pass
        else:
            break
    else:
        zero = True
    for num in list_num:
        if num <= 7:
            pass
        else:
            break
    else:
        week = True

    if month:
        return 50
    elif zero:
        return 0
    elif week:
        return 5
    else:
        return 10

def diagonal(list_of_lists):
    return [list_of_lists[i][i] for i in range(len(list_of_lists))]

def reverse_str(string):
    newStr = ''
    for i in range(len(string)):
        newStr += string[-1-i]
    return newStr

def remomve_negative(list_num):
    return [num for num in list_num if num > 0]

def add_matrix(matrix1, matrix2):
    return [[matrix1[row][col] + matrix2[row][col] for col in range(len(matrix1[row]))]for row in range(len(matrix1))]

matrix1 = [[1,2,3,4],
           [5,6,7,8],
           [9,1,2,3]]
matrix2 = [[9,8,7,6],
           [5,4,3,2],
           [1,9,8,7]]

def find_ordered_string(substring, string):
    i = 0
    for letter in string:
        if substring[i] == letter:
            i += 1
            if i == (len(substring)):
                return True
    return False


def getKthdigit(n,k):
    n = str(n)
    if k > len(n) - 1 or (n)[-1-k] == '-':
        return 0
    else:
        return n[-1-k]

def item(c):
    item_dict = {'t': 0.1, "p": 1.0, 'r': 3.0, 'g': 5.3, "l": 9.07}
    return item_dict[c]

def sentence_converter():
    sentence = input('Enter a Sentence: ')
    while len(sentence.split()) < 3:
        print('Must be More than 3 words')
        sentence = input('Enter a Sentence: ')
    max = 0
    words = sentence.split()
    for index, word in enumerate(words):
        if len(word) > max:
            max = len(word)
            max_word = word
        if 'o' in word.lower():
            words[index] = word.upper()
    print(' '.join(words))
    print(f'Longest Word is: {max_word}')

sentence_converter()