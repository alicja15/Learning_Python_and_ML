class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side*self.side
    def perimeter(self):
        return self.side*4
    
square1 = Square()

print(square1.area())
print(square1.perimeter())
