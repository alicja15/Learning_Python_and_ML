class Money:
    def __init__(self, amount, currency):
        self.amount = amount 
        self.currency = currency 
        
    def __str__(self):
        return (f"'{self.amount} {self.currency}'")
    
    def __add__(self, other):
        if self.currency == other.currency:
            return self.amount + other.amount
        else:
            raise ValueError("Currency mismatch")
    
    def __lt__(self, other):
        if self.currency == other.currency:
            return self.amount < other.amount
        else:
            raise ValueError("Currency mismatch")

#test 
m1 = Money(100, "PLN")
m2 = Money(50.5, "PLN")
m3 = Money(20, "USD")

try:
    print(m1+m2)#150.5
    print(m1<m2)#False
    print(m1<m3)#Currency mismatch
except ValueError as err:
    print(err)

    