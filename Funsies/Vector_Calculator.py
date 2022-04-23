import math

def vector_MagAndAngle(i, mag_list, angle_list):
    magnitude = float(input(f'Vector {i+1} Magnitude: '))
    mag_list.append(magnitude)
    angle = float(input(f'Vector {i + 1} Angle: '))
    if degrees:
        angle = angle*(math.pi/180)
    angle_list.append(angle)



mag_list = []
angle_list = []

n = int(input('Enter Number of Vectors: '))

while True:
    angle_type = input('Angle in (D)egrees or (R)adians?: ')

    if angle_type.upper() == 'D':
        degrees = True
        break
    elif angle_type.lower() == "R":
        degrees = False
        break
    else:
        print('Invalid Option')

for i in range(n):
    vector_MagAndAngle(i, mag_list, angle_list)

x_component_list = []
y_component_list = []

for i in range(n):
    x_component = mag_list[i]*math.cos(angle_list[i])
    x_component_list.append(x_component)
    y_component = mag_list[i]*math.sin(angle_list[i])
    y_component_list.append(y_component)

resultant_x = 0
for x in x_component_list:
    resultant_x += x

resultant_y = 0
for y in y_component_list:
    resultant_y += y

resultant_magnitude = ((resultant_x**2)+(resultant_y**2))**0.5
resultant_angle = (math.atan(resultant_y/resultant_x)) *(180/math.pi)

print('X Component of Resultant:', round(resultant_x,2))
print('Y Component of Resultant:', round(resultant_y,2))
print('Resultant Magnitude:', round(resultant_magnitude,2))
print('Resultant Angle in Degrees:', round(resultant_angle,2))


