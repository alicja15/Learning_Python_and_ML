from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, hours_worked):
        self.name = name 
        self.hours_worked = hours_worked
    @property
    def hours_worked(self):
        return self.__hours_worked
    @hours_worked.setter
    def hours_worked(self, value):
        if value >= 0:
            self.__hours_worked = value
        else:
            print("Hours cannot be negative")
    @abstractmethod
    def calculate_salary(self):
        pass
    def print_payslip(self):
        print(f"Employee: {self.name} | salary: {self.calculate_salary()}")

class FullTimeEmployee(Employee):
    def __init__(self, name, hours_worked, monthly_salary):
        super().__init__(name, hours_worked)
        self.monthly_salary = monthly_salary
    @property
    def monthly_salary(self):
        return self.__monthly_salary
    @monthly_salary.setter
    def monthly_salary(self, value):
        if value > 0:
            self.__monthly_salary = value
        else:
            print("Salary must be positive")
    def calculate_salary(self):
        return self.monthly_salary
class ContractEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name, hours_worked)
        self.hourly_rate = hourly_rate
    @property
    def hourly_rate(self):
        return self.__hourly_rate
    @hourly_rate.setter
    def hourly_rate(self, value):
        if value > 0:
            self.__hourly_rate = value
        else:
            print("Hourly rate must be positive")
    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked
    
class Intern(Employee):
    def calculate_salary(self):
        return "1500 PLN"


employees = [
    FullTimeEmployee("Adam Kowalski", 160, 5000),
    ContractEmployee("Anna Nowak", 120, 50),
    Intern("Marek Podbipięta", 80)
]

for employee in employees:
    employee.print_payslip()