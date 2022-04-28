################## Helper Code Below -- don't delete! ##################


# Helper Code 1
bach_data = []
with open("Bachelors.txt", "r") as f:
    for num in f:
        num = float(num.strip())
        bach_data.append(num)
f.close()


# Helper Code 2
pop_data = []
with open("Population.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        pop_data.append(value)
file.close()



# Helper Code 3
avg_income = []
with open("Income.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        avg_income.append(value)
file.close()



# Helper Code 4
high_school_data = []
with open("HighSchool.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        high_school_data.append(value)
file.close()


# Helper Code 5
poverty_data = []
with open("Poverty.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        poverty_data.append(value)
file.close()

# TASK 1

# QUESTION 1.1
def percent_bachelors(bach_data, pop_data):
    '''
    This function takes the bachelor's and population data
    for each county and returns the percentage of people
    with a bachelors or higher across all counties
    '''
    bs_sum = 0
    population = 0
    for i in range(len(bach_data)):
        bs_sum += ((bach_data[i]/100)*pop_data[i])
        population += pop_data[i]
    return (bs_sum / population) * 100

# QUESTION 1.2


def income_above_50k(avg_income):
    '''
    This function takes the average income of all counties
    and returns the percentage of counties with an income
    above $50,000
    '''
    total_county = 0
    for income in avg_income:
        if income > 50000:
            total_county += 1
    return (total_county/len(avg_income)) * 100


# ---------------------------------------------------------------------------------------------------- #


# TASK 2
def high_school_below_threshold(high_school_data, threshold):
    '''
    This function takes the percentage of high graduate in each county and
    returns the number counties with a percentage lower than a threshold number
    '''
    i = 0
    for x in high_school_data:
        if x < threshold:
            i += 1
    return i

# ---------------------------------------------------------------------------------------------------- #


# TASK 3
def bachelors_above_threshold(bach_data, threshold):
    '''
    This function takes the percentage of bachelor degree holders
    in all counties and returns the number of counties with a
    percentage higher than a threshold number
    '''
    i = 0
    for x in bach_data:
        if x > threshold:
            i += 1
    return i


# ---------------------------------------------------------------------------------------------------- #


# TASK 4


def below_poverty_total(poverty_data, pop_data):
    '''This function takes the percentage of people below poverty level in a county
    and the total population in a county and returns the total number of
    people below poverty level across all counties
    '''
    count = 0
    for i in range(len(poverty_data)):
        count += ((poverty_data[i]/100)*pop_data[i])
    return count

# ---------------------------------------------------------------------------------------------------- #


# TASK 5
def percent_below_poverty(poverty_data, pop_data):
    '''This function takes the total number of people
    below poverty level from the function above and
    returns the percentage of people living in poverty'''
    population = 0
    for x in pop_data:
        population += x
    return (below_poverty_total(poverty_data, pop_data) / population) * 100


# ---------------------------------------------------------------------------------------------------- #


# TASK 6
def education_vs_poverty(bach_data, poverty_data):
    '''This function takes the percentage of bachelor degrees and poverty
    level in each county and returns the average poverty level for
    counties with respect to a certain percentage of bachelors degree'''
    L1 = 0
    L2 = 0
    L3 = 0
    L4 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in range(len(bach_data)):
        if bach_data[i] < 10:
            L1 += poverty_data[i]
            count1 += 1
        elif 10 <= bach_data[i] < 20:
            L2 += poverty_data[i]
            count2 += 1
        elif 20 <= bach_data[i] < 30:
            L3 += poverty_data[i]
            count3 += 1
        elif 30 <= bach_data[i]:
            L4 += poverty_data[i]
            count4 += 1
    return f'Average Poverty Level:\nBachelors <10%: {(L1/count1)}%\nBachelors >=10% and <20%: {L2/count2}%\nBachelors >=20% and <30%: {L3/count3}%\nBachelors >=30: {L4/count4}%'


BS_Percentage = percent_bachelors(bach_data,pop_data)
print(f'National Percentage of People with a Bachelors: {BS_Percentage}%\n')

County_Percentage = income_above_50k(avg_income)
print(f"Percentage of Counties with an Average Income Higher than $50,000: {County_Percentage}%\n")

threshold = float(input('Enter a Threshold Percentage for High School Graduates: '))
total_number_of_counties = high_school_below_threshold(high_school_data, threshold)
print(f"Total Number of Counties with a Percentage of High School Graduate Below {threshold}%: {total_number_of_counties} Counties\n")

threshold = float(input('Enter a Threshold Percentage for BS Degree Holders: '))
total_BS_Counties = bachelors_above_threshold(bach_data, threshold)
print(f'Total Number of Counties with a Percentage of BS Degree Holders above {threshold}%: {total_BS_Counties} Counties \n')

total_number_below_poverty = below_poverty_total(poverty_data, pop_data)
print(f"Total Number of People Below Poverty Level: {total_number_below_poverty}\n")

percentage_poverty = percent_below_poverty(poverty_data, pop_data)
print(f'Percentage of People below Poverty Level: {percentage_poverty}\n')

national_averages = education_vs_poverty(bach_data,poverty_data)
print(national_averages)
