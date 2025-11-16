
# print("Hello, World!")

# print(10/0)

# try:
#     num = int(input("Enter the Number:"))
#     print(10/num)
# except ZeroDivisionError:
#     print("Number can not be divided by zero")
# except Exception as e:
#     print("Error occured : ", e)
# else:
#     print("code run without error")
# finally:
#     print("finally block run")

print("Enter the age greater than 18.")
age = int(input("Enter the age: "))

if age < 18:
    raise ValueError("Please enter the age above the 18.")

print("next code")