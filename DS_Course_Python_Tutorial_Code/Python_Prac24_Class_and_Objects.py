
# class Student:

#     name = ""
#     age = 0
#     city = ""

#     def display(self):
#         print("Name : ", self.name)
#         print("Age : ", self.age)
#         print("City : ", self.city)
        
# std1 = Student()
# std1.name = "Muhammad Ishfaq Khan"
# std1.age = 20
# std1.city = "Mianwali"

# std1.display()

# std2 = Student()
# std2.name = "Hammad Khan"
# std2.age = 25
# std2.city = "Karachi"

# std2.display()


class Employee:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        print("Employee Name: ", self.name)
        print("Employee Age: ", self.age)
        print("Employee City: ", self.city)

emp1 = Employee("Ishfaq Khan", 20, "Mianwali")
emp2 = Employee("Hammad Khan", 25, "Lahore")

print("Employee 1 Data: ")
emp1.display()

print("\nEmployee 2 Data: ")
emp2.display()
