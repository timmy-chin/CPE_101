import random

class Questions:
    def __init__(self,num, question):
        self.num = num
        self.question = question

with open('Num.txt', 'r') as file:
    num_list = [word.replace('\n', '') for word in file]

with open('Question.txt', 'r') as file:
    question_list = [word.replace('\\n', '\n') for word in file]

question_bank = [Questions(num_list[i], question_list[i]) for i in range(len(num_list))]

random.shuffle(question_bank)

for index, problem in enumerate(question_bank):
    number = problem.num
    print(f'MQ {number[0]}.{number[1]} Question {number[2:]}\n')
    print(f'{index+1}. {problem.question}\n\n\n')
