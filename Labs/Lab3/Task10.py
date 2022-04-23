def weight_of_item(char):
    character_list = ['t','p','r','g','l']
    mass_list = [0.1,1.0,3.0,5.3,9.07]

    for i in range(len(character_list)):
        if char == character_list[i]:
            return mass_list[i]
    return 0.0

print(weight_of_item(input('Enter Item Character: ')), 'KG')

