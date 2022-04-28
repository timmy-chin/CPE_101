from Project2 import *

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




