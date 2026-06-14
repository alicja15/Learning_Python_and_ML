class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Price must be positive")
    @property
    def price_with_tax(self):
        return round(self.__price * 1.23, 2)

p = Product("Stolik 234P", 349)
print(f"Product name: {p.name}")
print(f"Price: {p.price}")
print(f"Total with tax: {p.price_with_tax}")

