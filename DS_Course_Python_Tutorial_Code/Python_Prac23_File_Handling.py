
# file = open("Text_files/example.txt", 'a')

# content = "\nI am the new line added by using append mode."
# file.write(content)

# file.close()

# with open("Text_files/example.txt", 'a') as text_file:
#     content = "\nI am the new line added by using append mode with (with) statment."
#     text_file.write(content)

# import os 

# if os.path.exists("Text_files/example.txt"):
#     print("File found before remove")
# else:
#     print("file not found before remove")

# os.remove("Text_files/example.txt")

# if os.path.exists("Text_files/example.txt"):
#     print("File found after remove")
# else:
#     print("file not found after remove")

# # Writing data
# data = 'This is a sample text.'
# with open('Text_files/sample.txt', 'w') as file:
#     file.write(data)

# # Reading the same file
# with open('Text_files/sample.txt', 'r') as file:
#     content = file.read()
#     print(content)

# file = open("Text_files/example.txt", "r")

# try:
#     file = open("Text_files/example.txt", "r")
# except FileNotFoundError:
#     print("file not found plz first create the file")
# finally:
#     print("program finish")

import json

# student = {'name': 'Ishfaq', 'age': 22, 'city': 'Karachi'}
# with open('json_files/example.json', 'w') as file:
#     json.dump(student, file)

with open('json_files/example.json', 'r') as file:
    content = json.load(file)
    print(content)