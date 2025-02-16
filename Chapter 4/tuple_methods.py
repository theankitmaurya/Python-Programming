a = (1, 34, 7652, False, "Shivam", "YouTube")
print(a)

no = a.count(34)
print(no) # returns 1 | Returns the total value meaning how many times the given value is present in the tuple.

i = a.index("Shivam")
print(i) # returns 4 | Returns the index of the given value in the tuple. Also returns the first occurrence of the value.

print(len(a)) # returns 6 | Returns the length of the tuple.
