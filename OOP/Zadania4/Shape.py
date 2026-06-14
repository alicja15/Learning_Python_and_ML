from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print(f"Shape: {self.name}, Area: {self.area()}")
    
class Circle(Shape):
    def __init__(self, radius, name='Circle'):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.14*(self.radius**2)


class Rectangle(Shape):
    def __init__(self, height, width, name="Rectangle"):
        super().__init__(name)
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height
    
c = Circle(5)
r = Rectangle(4, 6)
c.describe() #Shape: Circle, Area: 78.5
r.describe() #Shape: Rectangle, Area: 24

try:
    test_shape = Shape("test")
except TypeError as err:
    print(f"Error ocurred: {err}")
#Error ocurred: Can't instantiate abstract class Shape without an implementation for abstract method 'area'

