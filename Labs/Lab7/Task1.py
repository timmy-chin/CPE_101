import math

class Shape:
    def __init__(self, name, dim):
        self.name = name
        self.dim = dim

class Dimension:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def cal_area(list):
    for area in list:
        if area.name == 'ellipse':
            A_list = [math.pi * dim.a * dim.b for dim in area.dim]
        else:
            A_list = [dim.a * dim.b for dim in area.dim]

        max = A_list[0]
        for num in A_list:
            if num > max:
                max = num

        print(f'{max} is the max area amongst all shapes of type: {area.name}')


Geometric_Shapes = [Shape('rectangle', [Dimension(5, 6), Dimension(14, 7), Dimension(5, 2)]), Shape('square', [Dimension(5, 5), Dimension(4.2, 4.2)]), Shape('ellipse', [Dimension(5, 6), Dimension(7, 7)])]

cal_area(Geometric_Shapes)