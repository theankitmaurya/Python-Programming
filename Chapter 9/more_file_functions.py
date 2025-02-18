f = open("file.txt")

lines = f.readlines()
print(lines, type(lines))

lines1 = f.readline()
print(lines1, type(lines1))

lines2 = f.readline()
print(lines2, type(lines2))

lines3 = f.readline()
print(lines3, type(lines3))

lines4 = f.readline()
print(lines4, type(lines4))

f.close()
