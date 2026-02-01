
# class person:

#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age = age
#         self.__salary = salary

#     def set_salary(self, salary):
#         self.__salary = salary

#     def get_salary(self):
#         print(self.__salary)

# p1 = person("Ishfaq", 25, 50000)

# print(p1.name)
# print(p1._age)
# p1.get_salary()

# p1._age = 20
# p1.set_salary(70000)

# print(p1.name)
# print(p1._age)
# p1.get_salary()

# class Demo:
#     def public_method(self):
#         print("Public method.")
#         # self._protected_method()

#     def _protected_method(self):
#         print("Protected method.")
#         self.__private_method()

#     def __private_method(self):
#         print("Private method.")

# d1 = Demo()
# d1.public_method()
# d1._protected_method()
# d1.__private_method()