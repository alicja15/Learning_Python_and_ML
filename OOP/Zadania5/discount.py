from abc import ABC, abstractmethod

class Discount(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def apply(self, price):
        pass
    def __call__(self, price):
        return self.apply(price)
    
class PercentDiscount(Discount):
    def __init__(self, name, percent):
        super().__init__(name)  
        self.percent = percent
    def apply(self, price):
        return price * (1 - self.percent/100)
    
class FixedDiscount(Discount):
    def __init__(self, name,amount):
        super().__init__(name)
        self.amount = amount
    def apply(self, price):
        if price - self.amount >= 0:
            return price - self.amount
        else:
            print("Value can't  be negative")

class BuyOneGetOne(Discount):
    def apply(self, price):
        return price / 2

discounts = [
    PercentDiscount("Black Friday", 20),
    FixedDiscount("Voucher", 50),
    BuyOneGetOne("Buy one get one free")
]

cena_poczatkowa = 200

print(f"Cena początkowa: {cena_poczatkowa} zł\n")
for discount in discounts:
    nowa_cena = discount(cena_poczatkowa)
    print(f"Zniżka: {discount.name}, Cena po rabacie: {nowa_cena} zł")

