
# def Double_the_num(x):
#     return x * 2

# Multiple = lambda x, y: x*y

# print(Multiple(5, 3))

# numbers = [10, 20, 35, 40, 55]
# Even_Number = list(filter(lambda x: x % 2 == 0 , numbers))
# print(Even_Number)

from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# Sum_Numbers = reduce(lambda x, y: x + y, numbers)
# print(Sum_Numbers)

# students = [("Ali", 22), ("Sara", 20), ("Ahmed", 25)]
# students.sort(key=lambda x: x[1])
# print(students)   

# def countdown(n): # 5 # 4 # 3 # 2 # 1
#     if n == 0:
#         print("Time's up!")
#     else:
#         print(n) # 5 # 4 # 3 # 2 # 1
#         countdown(n - 1) # 4 # 3 # 2 # 1 # 0

# countdown(5)

# 5! = 120

# 5 x 4 x 3 x 2 x 1 =  120

# 1! = 1
# 0! = 1

# def factorial(n): # 5 # 4 # 3 # 2 # 1
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1) # 4 # 3 # 2 # 1

# # 5 X 4 X 3 X 2 X 1 = 120

# print(factorial(5))   # Output: 120

import sys
print(sys.getrecursionlimit()) 

sys.setrecursionlimit(10000)
print(sys.getrecursionlimit()) 