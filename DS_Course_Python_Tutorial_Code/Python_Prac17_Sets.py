
# fruits = {"apple", "banana", "orange", "apple"}
# print(fruits)

# for fruit in fruits:
#     print(fruit)

# fruits.add("Mango")
# print(fruits)

# fruits.update(["grapes", "watermelon"])
# print(fruits)

# fruits.remove("apple")
# print(fruits)
# fruits.discard("Nashpati")
# fruits.pop()
# print(fruits)

# fruits.clear()
# print(fruits)

A = {1, 2, 3, 4}
B = {2, 3, 6, 7}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))

C = A.copy()
print(C)

X = {1, 2}
Y = {1, 2, 3, 4}
Z = {9, 8}

print(X.issubset(Y))
print(Y.issuperset(X))
print(Y.isdisjoint(X))
