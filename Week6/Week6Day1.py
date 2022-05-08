# class my2D():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# p1 = my2D(1,2)
# p2 = my2D(-5,2)
#
# # print(p1.x, p2.y)
# # print(p2.x, p1.y)
#
# class myhouse():
#     def __init__(self, w, d, R, G, C, name):
#         self.w = w
#         self.d = d
#         self.R = R
#         self.G = G
#         self.C = C
#         self.name = name
#
#     def __repr__(self):
#         return (f'({str(self.w)}, {str(self.d)}, {str(self.R)}, {str(self.G)}, {str(self.C)})')
#
#     def sayhi(self):
#         print(f'My name is {self.name}')
#
#     def __eq__(obj1, obj2):
#         return (obj1.w == obj2.w and obj1.d == obj2.d and obj1.R == obj2.R and obj1.G == obj2.G and obj1.C == obj2.C)
#
# house1 = myhouse(1,1,1,0,'R', 'Timmy Chin')
# house2 = myhouse(1,1,1,0,'R', 'Timmy Chin')
# house3 = myhouse(1,1,1,1,'R', 'Timmy Chin')
#
#
# print(f'Display the details for the house: {house1}')
#
# #To access a method inside a class, call the method using obj.methodname
# house1.sayhi()
#
# print(f'Comparing house 1 to house 2: {house1 == house2}')
# print(f'Comparing house 1 to house 3: {house1 == house3}')



class mypandas():
    def __init__(self, height, size, color, age, name):
        self.height = height
        self.size = size
        self.color = color
        self.age = age
        self.name = name

    def Aggressive(self):
        return self.size > 10 and self.height > 10

    def Name(self):
        return self.name
    def cute(self):
        return self.size < 10 and self.color != "Red"

    def eating(self):
        return self.size > 10

    def __repr__(self):
        print(f'Panda Name: {self.Name()}')
        print(f"Aggressive: {self.Aggressive()}")
        print(f'Cute: {self.cute()}')
        return f'Eating: {self.eating()}\n'

panda1 = mypandas(11,9,'Black and White', 50, 'Xingxing')
panda2 = mypandas(5,5,'Green', 50, 'KaiLian')
panda3 = mypandas(20,15,'Yello', 50, 'WenXin')
panda4 = mypandas(9,7,'Blue', 50, 'HaoChi')
panda5 = mypandas(9,11,'Red', 50, 'MeiLing')

pandas = [panda1,panda2,panda3,panda4,panda5]

for panda in pandas:
    print(panda)





