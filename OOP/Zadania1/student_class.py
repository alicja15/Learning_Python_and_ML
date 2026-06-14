from phone_class import Phone

class Student:
    def __init__(self, name, grades, phone):
        self.name = name
        self.grades = grades
        self.phone = phone

    def average(self):
        return sum(self.grades)/len(self.grades)
    
    def passed(self):
        if self.average() >= 3: 
            print("Passed")
        else:
            print("Failed")

my_phone = Phone("Samsung", "S4", 15)
Student1 = Student("Alice", [2,3,4,1,5,1,2], my_phone)
Student1.passed()
Student1.phone.call() #Dodatkowy output
