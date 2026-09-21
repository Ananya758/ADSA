class Example:
    x = 100 #data
    def display(self):
        print("This is example class display method")
obj = Example()
print(obj.x)
obj.display()

from math import pi
class Circle:
    r = 2
    def Area(self):
        return pi * self.r * self.r
    def Perimeter(self):
        return 2 * pi * self.r
c = Circle()
print(c.Area())
print(c.Perimeter())