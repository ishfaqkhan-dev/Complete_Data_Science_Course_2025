
student = {
    "Name" : "Ishfaq", 
    "Age" : 20, 
    "Country" : "Pakistan"
}

# student["Age"] = 23
# student["Grade"] = "A+"


# print(student["Name"])
# print(student["Age"])
# print(student["Country"])
# print(student["Grade"])
# print(student)

# student.pop("Age")
# print(student)

# student.popitem()
# print(student)

# student.clear()
# print(student)

# for key in student:
#     print(key)

# for values in student.values():
#     print(values)


# for key, value in student.items():
#     print(f"{key} : {value}")  


print(student.keys())
print(student.values())
print(student.items())

print(len(student))

student_marks = {
    "Marks" : 90
}

student.update(student_marks)
print(student)

