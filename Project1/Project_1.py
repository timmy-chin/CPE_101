def AQI_Good(high, low, value):
    return 50 / (high - low) * (value - low)


def AQI_Moderate(high, low, value):
    return ((100 - 51) / (high - low)) * (value - low) + 51


def AQI_Sensitive(high, low, value):
    return (150 - 101) / (high - low) * (value - low) + 101


def AQI_Unhealthy(high, low, value):
    return (200 - 151) / (high - low) * (value - low) + 151


def AQI_Very(high, low, value):
    return (300 - 201) / (high - low) * (value - low) + 201


def AQI_Hazardous(high, low, value):
    return (500 - 301) / (high - low) * (value - low) + 301


def calculate_AQI(range_list, value, i):
    good_upperRange = range_list[0]
    moderate_upperRange = range_list[1]
    sensitive_upperRange = range_list[2]
    unhealthy_upperRange = range_list[3]
    very_upperRange = range_list[4]
    hazardous_upperRange = range_list[5]

    if value <= good_upperRange:
        return round(AQI_Good(good_upperRange, 0, value))
    elif value <= moderate_upperRange:
        return round(AQI_Moderate(moderate_upperRange, good_upperRange + i, value))
    elif value <= sensitive_upperRange:
        return round(AQI_Sensitive(sensitive_upperRange, moderate_upperRange + i, value))
    elif value <= unhealthy_upperRange:
        return round(AQI_Unhealthy(unhealthy_upperRange, sensitive_upperRange + i, value))
    elif value <= very_upperRange:
        return round(AQI_Very(very_upperRange, unhealthy_upperRange + i, value))
    elif value <= hazardous_upperRange:
        return round(AQI_Hazardous(hazardous_upperRange, very_upperRange + i, value))


def error(range_list, value):
    hazardous_upperRange = range_list[5]
    if value < 0 or value > hazardous_upperRange:
        print('Error: Pollutant Concentration Out of Range')
        return True
    else:
        return False


def check_max(max_list):
    max = max_list[0]
    for x in max_list:
        if max <= x:
            max = x
    return max


def category(max_num):
    if 0 <= max_num <= 50:
        return 'Good'
    elif max_num <= 100:
        return 'Moderate'
    elif max_num <= 150:
        return 'Unhealthy for Sensitive Group'
    elif max_num <= 200:
        return 'Unhealthy'
    elif max_num <= 300:
        return 'Very Unhealthy'
    elif max_num <= 500:
        return 'Hazardous'


# def get_AQI(name, unit, upRanges_list, max_list, i=1.0):
#     x = True
#     while x:
#         C = float(input(f'Enter {name} Concentration in {unit}:'))
#         x = error(upRanges_list, C)
#         if not x:
#             AQI = calculate_AQI(upRanges_list, C, i)
#             print(f'AQI for {name}:', AQI, '\n')
#             max_list.append(AQI)


PM25_upRanges = [12.0, 35.4, 55.4, 150.4, 250.4, 500.4]
PM10_upRanges = [54, 154, 254, 354, 424, 604]
NO2_upRanges = [53, 100, 360, 649, 1249, 2049]
SO2_upRanges = [35, 75, 185, 304, 604, 1004]
CO_upRanges = [4.4, 9.4, 12.4, 15.4, 30.4, 50.4]