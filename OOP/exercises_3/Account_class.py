class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self.__balance
    
    def _change_balance(self, value):
        self.__balance += value 

    def deposit(self, value):
        if value > 0:
            self.__balance += value
        else:
            print("Deposit value must be positive!")
    def info(self):
        print(f"Account owner: {self.owner}, Balance: {self.__balance}")

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if 0 <= value <= 1:
            self.__interest_rate = value 
        else:
            print("Interest rate must be between 0 and 1")
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self._change_balance(interest)
    def info(self):
        super().info()
        print(f"Account type: Savings Account, Interest Rate: {self.interest_rate * 100}%")
    
class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.__overdraft_limit = overdraft_limit
    @property
    def overdraft_limit(self):
        return self.__overdraft_limit
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self._change_balance(-amount)
        else:
            print("Insufficient funds")


acc1 = SavingsAccount("Alice", 1000, 0.05)  
acc2 = CheckingAccount("Bob", 0, 300)
acc1.info()
acc1.apply_interest()
acc2.info()
acc2.withdraw(250)
acc2.info()
acc2.withdraw(400)
acc2.info()
