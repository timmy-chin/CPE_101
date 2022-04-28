bracket = [0, 0, 9950, 40525, 86375, 164925, 209425, 523600, 100000000000000]
tax = [0, 0.1, 0.12, 0.22, 0.24, 0.32, 0.35]
r_list = [0]
income = int(float((input('Enter your Income:'))))
for i in range(6):
    j = 1
    if i == 0:
        j = 0
    remainder = (bracket[i + 1] - bracket[i]) * tax[i] + r_list[i]
    r_list.append(remainder)
    if bracket[i + 1] + j <= income <= bracket[i + 2]:
        tax_paid = remainder + (income - bracket[i + 1]) * tax[i + 1]
        tax_bracket = str(int(tax[i + 1]*100)) + '%'
if income >= 0:
    print("An income of", income, "places you in the", tax_bracket, 'income bracket')
    print('The US Federal tax on a income of USD', income, 'is USD', tax_paid, 'tax')
else:
    print('Error, income must be a positive value or reasonable')
