
age = 22 

# match (age):
#     case 10 :
#         print("Your age is 10.")
#     case 12 :
#         print("Your age is 12.")
#     case 15 :
#         print("Your age is 15.")
#     case 18 :
#         print("Your age is 18.")
#     case 20 :
#         print("Your age is 20.")
#     case _:
#         print("Invalid Value")

marks = 77 

match marks:
    case m if m >= 90:
        print("Grade A")
    case m if m >= 80:
        print("Grade B")
    case m if m >= 70:
        print("Grade C")
    case m if m >= 60:
        print("Grade D")
    case _:
        print("Grade F")

    