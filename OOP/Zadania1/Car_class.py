
class Car:
    def __init__(self, brand, year, owner):
        self.brand = brand
        self.year = year
        self.owner = owner
    
    def description(self):
        print(f"Car brand: {self.brand}, year: {self.year}, owner: {self.owner}")

Car1 = Car("Toyota", 2012, "Mark Rogers")
Car1.description()

