#pollymorphism is many forms
#override only in polymorphism
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b)->None:
        self.l=l
        self.b=b
    def area(self):
        print(f"Rectangle area ={self.l*self.b}")
    def perimeter(self):
        print(f"Rectange perimeter = {2*(self.l + self.b)}")

r = Rectangle(10,20)
r.area()

class Circle(Shape):
    def __init__(self,r)->None:
        self.r= r
    def area(self):
        print(f"Rectangle area = {3.142* self.r*self.r}")