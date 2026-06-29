class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self._id = id
        
    def introduce(self):
        print(f"Hi! My name is {self.name} and I'm {self.age} years old. (ID: {self._id})")

class Student(Person):
    def __init__(self, name, age, id, grades):
        super().__init__(name, age, id)
        self.grades = grades
    def add_grade(self, grade):
        if 1 <= grade <= 6:
            self.grades.append(grade)
        else:
            print(f"Invalid grade value")
    def average(self):
        return round(sum(self.grades) / len(self.grades), 2)
    def introduce(self):
        super().introduce()
        print(f"I'm a student with a {self.average()} GPA")

class Teacher(Person):
    def __init__(self, name, age, id, subject):
        super().__init__(name, age, id)
        self.subject = subject
        self.__students_taught = []
 
    def add_student(self, student):
        self.__students_taught.append(student)
    
    def list_students(self):
        print(f"Students taught by {self.name}:")
        for student in self.__students_taught:
            print(f" - {student.name} (GPA: {student.average()})")
    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject}.")
        
    
#TEST KODUU
s1 = Student("Alice", 20, "123", [1,3,4,6])
s1.add_grade(5)
s1.add_grade(4)

s2 = Student("Bob", 21, "456", [5,6,3])
s2.add_grade(6)
s2.add_grade(5)


t = Teacher("Magdalena Nowak", 45, "TEACH1", "Mathematics")
t.add_student(s1)
t.add_student(s2)


t.introduce()
t.list_students()
s1.introduce()