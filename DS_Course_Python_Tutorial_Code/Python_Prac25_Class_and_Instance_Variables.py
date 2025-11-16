
class Student:

    school = "Govt High School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("School: ", self.school)
        

Student.school = "ABC High School"

std1 = Student("Ishfaq", 20)
std2 = Student("Hammad", 25)
std3 = Student("Sajjad", 23)

std3.school = "XYZ School"

print("Student no 1:")
std1.display()

print("\nStudent no 2:")
std2.display()

print("\nStudent no 3:")
std3.display()

