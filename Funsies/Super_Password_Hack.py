import time

Password = 'abc1'

char_list = [chr(i) for i in range(32,127)]

def super_hack(Password):
    for word1 in char_list:
        for word2 in char_list:
            for word3 in char_list:
                for word4 in char_list:
                    for word5 in char_list:
                        for word6 in char_list:
                            password = str(word3) + str(word4) + str(word5) + str(word6)
                            print(password)
                            if password == Password:
                                return password


start_time = time.time()
print(f'Password is {super_hack(Password)}')
print(f'Time is Took to Crack Password: {time.time() - start_time} seconds')


