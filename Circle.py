import math
class Circle:
    def __init__(self,r):
        self.__radius=r

    def SetRadius(self):
        self.__radius=int(input("Enter the radius  of circle: "))
        
    def GetRadius(self):
        print("The radius is",self.__radius)

    def GetArea(self):
        Area=math.pi*(self.__radius*self.__radius)
        print("Area1 =",Area)
        return Area
Circle1=Circle(20)

Circle1.GetRadius()

Circle1.SetRadius()
Circle1.GetRadius()

Circle1.GetArea()

class Cylinder(Circle):
    def __init__(self,r):
        super().__init__(r)
        self.__height=0
    def SetHeight(self):
        self.__height=int(input("Enter the height: "))
        
    def GetHeight(self):
        print("The height is",self.__height)

    def Volume(self):
        Volume1=super().GetArea() * self.__height
        print("Volume=",Volume1)
        
Cylinder1=Cylinder(20)
Cylinder1.SetHeight()
Cylinder1.Volume()
