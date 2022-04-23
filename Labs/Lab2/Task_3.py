income = int(float(input('Enter Income:')))
bracket = ''
if 0 <= income <= 9950:
    bracket += '10%'
    tax = income*0.1
elif 9951 <= income <= 40525:
    bracket += '12%'
    tax = 995+ (income - 9950) * 0.12
elif 40526 <= income <= 86375:
    bracket += '22%'
    tax = 4664 + (income - 40525) * 0.22
elif 86376 <= income <= 164825:
    bracket += '24%'
    tax = 14751 + (income - 86375) * 0.24
elif 164926 <= income <= 209425:
    bracket += '32%'
    tax = 33603 + (income - 164925) * 0.32
elif 209426 <= income <= 523600:
    bracket += '35%'
    tax = 47843 + (income - 209425) * 0.35
elif income >= 523601:
    bracket += '37%'
    tax = 157804.24 + (income - 523600) * 0.37


if income >= 0:
    print("An income of", income, "places you in the", bracket, 'income bracket')
    print('The US Federal tax on a income of USD',income, 'is USD', tax, 'tax')

else:
    print('Error, income must be a positive value')



