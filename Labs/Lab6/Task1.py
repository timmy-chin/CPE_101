import math

class my3D:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def __eq__(obj1, obj2):
        return obj1.x == obj2.x and obj1.y == obj2.y and obj1.z == obj2.z and obj1.r == obj2.r

    def volume(self):
        return (4/3)*(math.pi)*((self.r)**3)


def volume_ratio(obj1, obj2):
    volume1 = obj1.volume()
    volume2 = obj2.volume()
    if volume1 > volume2:
        return f'Sphere-1 is {volume1/volume2} times bigger than Sphere-2'
    elif volume1 < volume2:
        return f'Sphere-2 is {volume2 / volume1} times bigger than Sphere-1'
    elif volume1 == volume2:
        return f'Sphere-1 has the same volume as Sphere-2'


def collide_identical(obj1, obj2):
    if obj1 == obj2:
        return '\nThe Spheres are Identical'
    elif obj1.r + obj2.r >= ((obj2.x - obj1.x)**2 + (obj2.y - obj1.y)**2 + (obj2.z - obj1.z)**2)**1/2:
        return "\nThe Sphere Collide!!!"
    else:
        return f'\nThe Spheres do not collide!!!\n{volume_ratio(obj1, obj2)}'

print('\nEnter Detail for First Sphere:')
Sphere1 = my3D(float(input('Sphere-1 x: ')), float(input('Sphere-1 y: ')), float(input('Sphere-1 z: ')), float(input('Sphere-1 radius: ')))
print('\nEnter Detail for Second Sphere:')
Sphere2 = my3D(float(input('Sphere-2 x: ')), float(input('Sphere-2 y: ')), float(input('Sphere-2 z: ')), float(input('Sphere-2 radius: ')))

print(collide_identical(Sphere1, Sphere2))