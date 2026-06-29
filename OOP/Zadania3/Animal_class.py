class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Woof or Meow!")

    def info(self):
        print(f"This is {self.name} and it's {self.age} years old! :)")

class Dog(Animal):

    def make_sound(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} wants to play fetch!")

class Cat(Animal):

    def make_sound(self):
        print("Meow!")

    def scratch(self):
        print(f"{self.name} just scratched your couch!")

        
#TEST KODU
dog = Dog("Burek", 5)
cat = Cat("Mruczek", 3)

dog.info()
dog.make_sound() 
dog.fetch()

print("-" * 20)

cat.info()
cat.make_sound() 
cat.scratch()