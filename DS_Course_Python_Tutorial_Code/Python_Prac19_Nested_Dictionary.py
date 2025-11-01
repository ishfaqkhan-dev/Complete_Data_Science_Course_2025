
import copy

students = {
    "student1" : {
        "name" : "Ali",
        "age" : 20,
        "city" : "Lahore"
    },
    "student2" : {
        "name" : "Ishfaq",
        "age" : 21,
        "city" : "Mianwali"
    }
}

new_Students_dic = copy.deepcopy(students)
new_Students_dic["student1"]["name"] = "Saqib"
print(new_Students_dic)
print(students)


# students["student3"] = {
#     "name" : "Kaif",
#     "age" : 23,
#     "city" : "Bannu"
# }

# print(students.items())
# print(students["student1"].items())

# for outer_key, outer_value in students.items():
#     print(outer_key)
#     for inner_key, inner_value in outer_value.items():
#         print(f"Inner Key : {inner_key} : Inner Value : {inner_value}")

# students["student2"]["country"] = "Pakistan"

# print(students["student1"]["age"])
# print(students["student1"])
# print(students["student2"]["name"])
# print(students["student2"])
# print(students["student3"])

# del students["student1"]
# del students["student1"]["age"]


# print(students["student1"])



# print(students)