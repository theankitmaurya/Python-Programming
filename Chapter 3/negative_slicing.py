name = "Ankit"

print(name[0:3])

print(name[-4 : -1]) #This will return the same output as below one returns

print(name[1 : 4]) #This will return the output as 'nki' | Start from index 1 all the way till 4th (excluding 4th)

# ✅ To get the negative indexing write its corresponding positive index and then replace it with negative index

# ✅ Example: A, N, K, I, T
# ✅ Positive Index: 0, 1, 2, 3, 4
# ✅ Negative Index: -5, -4, -3, -2, -1

# Here, A -> 0, -5
#       N -> 1, -4
#       K -> 2, -3
#       I -> 3, -2
#       T -> 4, -1

# ✅ Positive Index starts with -> 0
# ✅ Negative Index starts with -> -1

print(name[ : 4]) # returns 'Anki' | Start from index 0 all the way till 4th (excluding 4th) | This is same as print(name[0 : 4])
print(name[1 : ]) # returns 'nkit' | Start from index 1 all the way till the end | This is same as print(name[1 : 5])
print(name[1 : 5]) # returns 'nkit' | Start from index 1 all the way till end


# Slicing with skip value
# Format -> s2 = name[ind_start:ind_end:skip_val]

word = "amazing"

z = word[1 : 6 : 2] # returns 'mzn' | Start from index 1 all the way till 6th (excluding 6th) with a skip value of 2

print(z)
