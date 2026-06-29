class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0
    
    def describe(self):
        print(f"Shape: {self.name}, Area: {self.area()}")
        
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(name='Circle')
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Radius must be positive!")

    def area(self):
        return 3.14*(self._radius**2)
    
class Rectangle(Shape):
    def __init__(self, width, height, name="Rectangle"):
        super().__init__(name=name)
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    
class Square(Rectangle):
        def __init__(self, side):
            super().__init__(width=side, height=side, name="Square")
            self.side = side
        
c = Circle(5)
r = Rectangle(4, 6)
s = Square(3)

shapes = [c, r, s]

for shape in shapes:
    shape.describe()