myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1st Method -> This is the first method and long method too
squaredList = []
for item in myList:
    squaredList.append(item * item)

print(f"1 -> {squaredList}")

# 2nd Method -> The above thing can be done using list comprehension in short way and in only one line
squaredList = [i * i for i in myList]
print(f"2 -> {squaredList}")
