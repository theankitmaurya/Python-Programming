l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1st Method -> This is long process
index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

# 2nd Method -> Using enumerate() function
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")
