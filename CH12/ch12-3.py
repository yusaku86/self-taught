class Triangle:
    def __init__(self,l,h):
        self.len = l
        self.height = h
    def area(self):
        return self.len * self.height /2

triangle = Triangle(3,5)
print(triangle.area())