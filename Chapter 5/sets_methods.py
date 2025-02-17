# Properties of Sets ->
# 1. Sets are unordered => Elements order doesn't matter
# 2. Set elements are uniindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

# Methods in Sets
s = {1, 2, 25, 32, "Ankit", 45.6}

# 1. add() -> Adds an element to the set
s.add(50)
print(s, type(s))

# 2. copy() -> Returns a copy of the set
s1 = s.copy()
print(s1, type(s1))

# 3. difference() -> Returns a set containing the difference between two or more sets
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}
s4 = s2.difference(s3)
print(s4)

# 4. clear() -> Removes all elements from the set
s.clear()
print(s)

# Operations on Sets ->
s = {1, 8, 2, 3}

# 1. len(s) -> Returns the length of the set
o = len(s)
print(o)

# 2. s.remove() -> Updates the set 's' and removes 'something' from 's'
s.remove(8)
print(s)

# 3. s.pop() -> Removes an arbitrary element from the set and return the element removed
s.pop()
print(s)

# 4. s.union() -> Returns a new set with all items from both sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s3 = s1.union(s2)
print(s3)

# 5. s.intersection() -> Returns a set which contains only item in both sets
s4 = s1.intersection(s2)
print(s4)

# 6. s.clear() -> Removes all elements from the set
s.clear()
print(s)

# 7. s.add() -> Adds an element to the set
s.add(50)
print(s)

# 8. s.differece() -> Returns a set containing the difference between two or more sets
s5 = s1.difference(s2)
print(s5)
