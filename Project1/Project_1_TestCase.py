from Project_1 import *

def get_AQI(name, unit, upRanges_list, max_list, test_num):
    x = True
    while x:
        C = test_num
        print('Test Value:', C)
        x = error(upRanges_list, C)
        if not x:
            AQI = calculate_AQI(upRanges_list, C)
            print(f'AQI for {name}:', AQI, '\n')
            max_list.append(AQI)
            print('Category:', category(AQI),'\n')

test_PM25 = [10,20,40,80,200,300,30]
test_PM10 = [20, 80, 200, 300, 355, 500,30]
test_NO2 = [20, 80, 200, 400, 700, 1300,30]
test_SO2 = [20, 50, 100, 200, 400, 800,30]
test_CO = [3,6,9.5,13,30.4,40,40]
# location = input('Enter Location:')

for i in range(len(test_CO)):
    max_list = []

    get_AQI('PM_2.5', 'ug/m3', PM25_upRanges, max_list, test_PM25[i])
    get_AQI('PM_10', 'ug/m3', PM10_upRanges, max_list, test_PM10[i])
    get_AQI('NO2', 'ppb', NO2_upRanges, max_list, test_NO2[i])
    get_AQI('SO2', 'ppb', SO2_upRanges, max_list, test_SO2[i])
    get_AQI('CO', 'ppm', CO_upRanges, max_list, test_CO[i])

    max = check_max(max_list)

    print('Final AQI:', max)
    print('Category:', category(max))
    print('\n\n\n')




