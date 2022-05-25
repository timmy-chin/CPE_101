f = open('OG_Image.ppm', 'r')

rgb_lst = [line for line in f]


# start from index 3 when using lst

for i in range(3, len(rgb_lst)):
    rgb_lst[i] = rgb_lst[i].split()

for i in range(3, len(rgb_lst)):
    tripplet = [rgb_lst[i][j:j+3] for j in range(0, len(rgb_lst[i]), 3)]
    rgb_lst[i] = tripplet

negated_lst = list(rgb_lst)

gray_lst = list(rgb_lst)

no_red = list(rgb_lst)



def negate_color(lst):
    for i in range(3, len(lst)):
        for rgb in lst[i]:
            for j in range(len(rgb)):
                rgb[j] = str(255 - int(rgb[j]))
    return lst

def gray_scale(lst):
    for i in range(3, len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = lst[i][j].split()
            print(lst[i][j])
            # sum = 0
            # for j in range(len(rgb)):
            #     sum += int(rgb[j])
            # avg = int(sum / 3)
            # for a in range(len(rgb)):
            #     rgb[a] = str(avg)

    return lst

def remove_red(lst):
    for i in range(3, len(lst)):
        for rgb in lst[i]:
            rgb = rgb.split()
            rgb[0] = str(0)

    return lst

def make_into_lines(lst):
    for i in range(3, len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = ' '.join(lst[i][j])

    for i in range(3, len(lst)):
        lst[i] = ' '.join(lst[i])

    return lst




negated_lst = negate_color(negated_lst)


negated_lst = make_into_lines(negated_lst)

w = open('nny.ppm', 'w')


for word in negated_lst:
    w.write(word +'\n')
w.close()


w3 = open('nnnny.ppm', 'w')

no_red = remove_red(no_red)

no_red = make_into_lines(no_red)

for word in no_red:
    w3.write(word+'\n')
w3.close()


gray_lst = gray_scale(gray_lst)

gray_lst = make_into_lines(gray_lst)

w2 = open('nnny.ppm', 'w')

for word in gray_lst:
    w2.write(word +'\n')
w2.close()





f.close()