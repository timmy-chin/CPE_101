def find_ordered_substring(substring, main):
    i = 0
    k = 0
    for x in substring.lower():
        for j in range(len(main)):
            if i <= j and x == main.lower()[j]:
                i = j
                k += 1
                break

    if k == len(substring):
        return True
    else:
        return False

print(find_ordered_substring(input('Substring: '),input('Main: ')))


# def find_ordered_substring(substring, main):
#     previous_index = 0
#     count = 0
#     for sub_letter in substring:
#         for i, main_letter in enumerate(main):
#             if sub_letter == main_letter and previous_index <= i:
#                 previous_index = i
#                 count += 1
#                 break
#     if count == len(substring):
#         return True
#     else:
#         return False

print(find_ordered_substring(input('Substring: '),input('Main: ')))
