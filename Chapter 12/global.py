a = 50
b = 100

def Fun():
    global a
    a = 10
    print(a)

Fun()
print(a)

print(b)

# The 'global' keyword is used to modify the variable outside of the current scope.
