from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.amount} PLN"

class CashPayment(Payment):
    def process(self):
        print(f"Paying {self.amount} in cash")

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    def process(self):
        print(f"Paying {self.amount} with card ****{self.card_number[-4:]}")

payment1 = CashPayment(50)
payment2 = CardPayment(120.50, "12345678912345678")

print(payment1) #CashPayment: 50 PLN
print(payment2) #CardPayment: 120.5 PLN

payment1.process() #Paying 50 in cash
payment2.process() #Paying 120.5 with card ****5678

