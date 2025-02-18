# A random-access memory is volatile, and all its contents are lost once a program terminates in order to persist the data forever, we use files.

# A file is data stored in a storage device. A python can talk to the file by reading content from it and writing content to it.

# Types of Files -> 2 types of files:
# 1. Text Files: .txt, .c, .py etc.
# 2. Binary files: .jpg, .dat etc.

# Format Code to open and read the file and closing the file
f = open("file.txt")
data = f.read()

print(data)

f.close()
