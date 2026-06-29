from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def make_sound(self):
        pass

    def introduce(self):
        return (f"Hello! My name is {self.name}! {self.make_sound()} {self.make_sound()}")

class Dog(Animal):

    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):

    def make_sound(self):
        return "Meow!"
    
animals = [Dog("Rex"), Cat("Whiskers")]

for animal in animals:
    print(animal.introduce())
#Hello! My name is Rex! Woof! Woof!
#Hello! My name is Whiskers! Meow! Meow!
