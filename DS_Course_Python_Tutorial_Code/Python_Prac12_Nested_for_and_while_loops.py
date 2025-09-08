
# for count1 in range(3):
#     print("Outer loop :", count1)
#     for count2 in range(5):
#         print("Inner loop :", count2)


i = 1
while i <= 3:
    j = 1
    print("Outer loop :", i)
    while j <= 5:
        print("Inner loop :", j)
        j = j + 1
    i = i + 1