
# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)

# class Student(Person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no

#     def display_roll(self):
#         print("Student Roll No:", self.roll_no)

#     def study_hours(self, hours):
#         self.hours = hours
#         print("Study Hours:", self.hours)

# class Employee(Person):
#     def __init__(self, name, age, id_no):
#         super().__init__(name, age)
#         self.id_no = id_no

#     def display_id(self):
#         print("Employee ID:", self.id_no)

#     def job_hours(self, hours):
#         self.hours = hours
#         print("Job Hours:", self.hours)

# # per1 = Person("Sajjad", 23)
# # per1.display()

# std1 = Student("Ishfaq", 20, 11)
# emp1 = Employee("Hammad", 25, "Emp05x")

# print("Student Data:")
# std1.display()
# std1.display_roll()
# std1.study_hours("6 Hours")

# print("\nEmployee Data:")
# emp1.display()
# emp1.display_id()
# emp1.job_hours("9 Hours")

# ===== > Multiple Inheritance < ======

# class A:
#     def funA(self):
#         print("Function A")

# class B:
#     def funB(self):
#         print("Function B")

# class C(A, B):
#     pass

# obj = C()
# obj.funA()
# obj.funB()

# ====== > Multilevel Inheritance < =======

class A:
    def funA(self):
        print("Function A")

class B(A):
    def funB(self):
        print("Function B")

class C(B):
    def funC(self):
        print("Function C")

obj = C()
obj.funA()
obj.funB()
obj.funC()