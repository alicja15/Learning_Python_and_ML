class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value 
        else:
            print("Salary can't be negative")

    def info(self):
        print(f"Employee: {self.name} earns {self.salary}")

    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    @property
    def bonus(self):
        return self.__bonus
    @bonus.setter
    def bonus(self, value):
        if value >= 0:
            self.__bonus = value
        else:
           print("Bonus can't be negative")
           
    @property
    def total_compensation(self):
        return self.salary + self.bonus
    
    def info(self):
        print(f"Employee: {self.name} earns {self.salary} with a {self.bonus} bonus. ({self.total_compensation} in total)")

#TESSST 
my_emp = Employee("Alice", 3500)
m = Manager("Alicja", 5000, 1000)
my_emp.info()
m.info()
