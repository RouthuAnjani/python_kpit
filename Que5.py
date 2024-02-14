import math
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    def type_of_shape(self):
        pass
class Square(Shape):
    def area(self,a):
        return a*a
    def type_of_shape(self):
        print("I am Square")
class Circle(Shape):
    def area(self,r):
        return (math.pi)*(r^2)
    def type_of_shape(self):
        print("I am Circle")
s=Square()
print("Area of square: ",s.area(2))
c=Circle()
print("Area of Circle: ",c.area(7))


class Triangle(Shape):
    def area(self,base,height):
        return (1/2)*base*height
    def type_of_shape(self):
        print("I am Triangle")
t=Triangle()
print("Area of triangle: ",t.area(10,20))
s.type_of_shape()
c.type_of_shape()
t.type_of_shape()