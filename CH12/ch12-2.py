import math
class Circle:
    def __init__(self,l):
        self.len = l
    
    def area(self):
        return self.len **2 * math.pi
circle = Circle(3)
print(circle.area()) 