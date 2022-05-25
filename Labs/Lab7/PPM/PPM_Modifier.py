with open('TextFiles/PPM_OG.txt', 'r') as file:
    RGB = [word for word in file]

file.close()

for i in range(3, len(RGB)):            #Group RGB values into list
    list_num = RGB[i].split()
    grouped_list = [list_num[i:i+3] for i in range(0,len(list_num), 3)]
    RGB[i] = grouped_list


# Modify 1: Negate Color

Negated_RGB = list(RGB)

for i in range(3, len(Negated_RGB)):
    negated_values = [[str(255 - int(num)) for num in RGB] for RGB in Negated_RGB[i]]
    Negated_RGB[i] = negated_values

for i in range(3, len(Negated_RGB)):        #Convert to Writeable Format
    join_str = [' '.join(RGB) for RGB in Negated_RGB[i]]
    join_str.append('\n')
    join_str = ' '.join(join_str)
    Negated_RGB[i] = join_str

with open('TextFiles/Negated_PPM.txt', 'w') as file:
    for word in Negated_RGB:
        file.write(word)

file.close()


#Modify 2: Grayscale

Grayscale_RGB = list(RGB)

for i in range(3, len(Grayscale_RGB)):
    grayscale_values = [[str(round((int(RGB[0]) + int(RGB[1]) + int(RGB[2]))/3)) for num in RGB] for RGB in Grayscale_RGB[i]]
    Grayscale_RGB[i] = grayscale_values

for i in range(3, len(Grayscale_RGB)):        #Convert to Writeable Format
    join_str = [' '.join(RGB) for RGB in Grayscale_RGB[i]]
    join_str.append('\n')
    join_str = ' '.join(join_str)
    Grayscale_RGB[i] = join_str

with open('TextFiles/Grayscale_PPM.txt', 'w') as file:
    for word in Grayscale_RGB:
        file.write(word)

file.close()



#Modify 3: Remove Prime Color Red

Prime_RGB = list(RGB)

for i in range(3, len(Prime_RGB)):
    for RGB in Prime_RGB[i]:
        RGB[1] = str(0)

for i in range(3, len(Prime_RGB)):        #Convert to Writeable Format
    join_str = [' '.join(RGB) for RGB in Prime_RGB[i]]
    join_str.append('\n')
    join_str = ' '.join(join_str)
    Prime_RGB[i] = join_str

with open('TextFiles/Prime_PPM.ppm', 'w') as file:
    for word in Prime_RGB:
        file.write(word)

file.close()



