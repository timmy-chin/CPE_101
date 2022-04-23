from Project_1 import *

location = input('Enter Location:')

max_list = []

get_AQI('PM_2.5', 'ug/m3', PM25_upRanges, max_list, 0.1)
get_AQI('PM_10', 'ug/m3', PM10_upRanges, max_list)
get_AQI('NO2', 'ppb', NO2_upRanges, max_list)
get_AQI('SO2', 'ppb', SO2_upRanges, max_list)
get_AQI('CO', 'ppm', CO_upRanges, max_list, 0.1)

max = check_max(max_list)

print('Location:', location)
print('Final AQI:', max)
print('Category:', category(max))





