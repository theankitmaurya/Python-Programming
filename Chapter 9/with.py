# f = open("file.txt")
# print(f.read())
# f.close()

# The same can be written using 'with' statement like this:
with open("file.txt") as f:
    print(f.read())

# By this we don't have to take burden of closing the file by writing the code. Due to using 'with' statement the file will automatically gets closed right after we leaves the code.
