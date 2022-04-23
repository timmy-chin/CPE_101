def cumulative(list_num):
    cumulative_list = []
    for i in range(len(list_num)):
        sum = 0
        while i >= 0:
            sum += list_num[i]
            i -= 1
        cumulative_list.append(sum)
    return cumulative_list

