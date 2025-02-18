# Write a python program to rename a file to "rename_by_python.txt".

with open("before_rename.txt") as f:
    content = f.read()

with open("rename_by_python.txt", "w") as f:
    f.write(content)
