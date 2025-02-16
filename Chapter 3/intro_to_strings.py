a = 'Ankit' #1st way to define a string

b = "Ankit" #2nd way to define a string

c = '''Ankit''' #3rd way to define a string

name = "Ankit"

print(len(name)) #len function returns the length of the string

# Slicing using the index
# Format -> s1 = name[ind_start:ind_end]
# ind_start is included and ind_end is not included

# Negative Indices: Negative indices can also be used. -1 corresponds to the (length - 1)index, -2 to (length - 2)index and so on.

shortName = name[0:3] #This will return 'Ank' | Start from index 0 all the way till 3rd (excluding 3rd)
print(shortName) 
