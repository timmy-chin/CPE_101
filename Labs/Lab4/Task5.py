import random

head = 0
tail = 0
for i in range(150):
    num = random.random()
    if num < 0.5:
        result = "Heads"
        head += 1
    else:
        result = "Tails"
        tail += 1
    print(result)

print(f'\nHeads Count: {head}')
print(f'Tails Count: {tail}')

print(f'Probability for Head: {round((head / (head + tail))*100)}%')
print(f'Probability for Tail: {round((tail / (head + tail))*100)}%')

