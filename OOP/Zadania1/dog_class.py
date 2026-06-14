
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"Woof! I am {self.name}")

doggo1 = Dog("Rex", "Yorkshire Terrier")
doggo1.bark()

