class Square:
    square_list = []

    def __init__(self,l):
        self.len = l
        self.square_list.append(self)
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len,self.len,self.len,self.len)

sq1 = Square(12)
sq2 = Square(15)
sq3 = Square(66)
print(sq1)
print(sq2)
print(sq3)