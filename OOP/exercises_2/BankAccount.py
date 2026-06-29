class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self._account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            return "Invalid amount"
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Insufficient funds"
    def show_balance(self):
        print(f"Your current balance is: {self.__balance}")

my_account = BankAccount("Alicja", 22193, 50123)
my_account.deposit(500)
my_account.withdraw(50000)
my_account.show_balance()
