#  1. len() function: This function returns the length of the string.
a = "Ankit"
b = len(a) 
print(b) # returns 5

# 2. String.endswith(): This function returns True if the string ends with the specified value, otherwise it returns False.
print(a.endswith("it")) # returns True

# 3. String.startswith(): This function returns True if the string starts with the specified value, otherwise it returns False.
print(a.startswith("An")) # returns True

# 4. String.capitalize(): This function returns a string with the first character capitalized and the rest lowercased.
c = "this is capitalized"
print(c.capitalize()) # returns 'This is capitalized'

# 5. String.count(): This function returns the number of times a specified value occurs in a string.
print(c.count("i")) # returns 4

# 6. String.find(): This function returns the index of the first occurrence of the specified value in the string.
d = "hello world"
index = d.find("world")
print(index) # returns 6

# 7. String.replace(old word, new word): This function replaces a specified value with another value in a string. It changes all the occurences of the old word with the new word.
e = "hello world"
replaced_string = e.replace("world", "Python")
print(replaced_string) # returns 'hello Python'

# 8. String.upper(): This function returns the string in uppercase.
f = "hello world"
upper_string = f.upper()
print(upper_string)  # returns 'HELLO WORLD'

# 9. String.lower(): This function returns the string in lowercase.
g = "HELLO WORLD"
lower_string = g.lower()
print(lower_string) # returns 'hello world'

# 10. String.split(): This function splits the string into substrings if it finds instances of the separator.
h = "hello,world"
splitted_string = h.split(",")
print(splitted_string) # returns ['hello', 'world']

# 11. String.strip(): This function removes any leading (spaces at the beginning) and trailing (spaces at the end) characters.
i = "   hello world   "
stripped_string = i.strip()
print(stripped_string) # returns 'hello world'

# 12. String.isalpha(): This function returns True if all the characters in the string are alphabets, otherwise it returns False.
j = "hello"
print(j.isalpha()) # returns True

# 13. String.isdigit(): This function returns True if all the characters in the string are digits, otherwise it returns False.
k = "123"
print(k.isdigit()) # returns True

# 14. String.isalnum(): This function returns True if all the characters in the string are alphanumeric, otherwise it returns False.
l = "hello123"
print(l.isalnum()) # returns True

# 15. String.islower(): This function returns True if all the characters in the string are lowercase, otherwise it returns False.
m = "hello"
print(m.islower()) # returns True

# 16. String.isupper(): This function returns True if all the characters in the string are uppercase, otherwise it returns False.
n = "HELLO"
print(n.isupper()) # returns True

# 17. String.isspace(): This function returns True if all the characters in the string are whitespaces, otherwise it returns False.
o = "   "
print(o.isspace()) # returns True

# 18. String.join(): This function joins the elements of an iterable (such as a list) with the string as a separator.
p = ["hello", "world"]
joined_string = " ".join(p)
print(joined_string) # returns 'hello world'

# 19. String.swapcase(): This function swaps the case of the characters in the string, i.e., converts lowercase characters to uppercase and vice versa.
q = "Hello World"
swapped_string = q.swapcase()
print(swapped_string) # returns 'hELLO wORLD'

# 20. String.title(): This function converts the first character of each word to uppercase and the rest to lowercase.
r = "hello world"
title_string = r.title()
print(title_string) # returns 'Hello World'

# 21. String.zfill(): This function pads the string with zeros to make it a specified length.
s = "42"
zfilled_string = s.zfill(5)
print(zfilled_string) # returns '00042'

# 22. String.center(): This function centers the string within a specified width.
t = "hello"
centered_string = t.center(10)
print(centered_string) # returns '  hello   '

# 23. String.ljust(): This function left aligns the string within a specified width.
u = "hello"
left_aligned_string = u.ljust(10)
print(left_aligned_string) # returns 'hello     '

# 24. String.rjust(): This function right aligns the string within a specified width.
v = "hello"
right_aligned_string = v.rjust(10)
print(right_aligned_string) # returns '     hello'

# 25. String.rfind(): This function returns the highest index of the first occurrence of the specified value in the string.
w = "hello world"
highest_index = w.rfind("o")
print(highest_index) # returns 7


# Escape Sequence Characters
# 1. \n: New line
a = "Ankit is a good boy\nand studying in college"

print(a) # returns 'Ankit is a good boy' in one line and 'and studying in college' in the next line

# 2. \t: Tab
b = "Ankit\tis\ta\tgood\tboy"

print(b) # returns 'Ankit   is   a   good   boy'

# 3. \': Single quote
c = "Ankit\'s book"

print(c) # returns 'Ankit's book'

# 4. \": Double quote
d = "Ankit\"s book"

print(d) # returns 'Ankit"s book'

# 5. \\: Backslash
e = "Ankit\\book"

print(e) # returns 'Ankit\book'

# 6. \b: Backspace
f = "Ankit\bbook"

print(f) # returns 'Ankibook'

# 7. \r: Carriage return
g = "Ankit\rbook"

print(g) # returns 'bookt'

# 8. \f: Form feed
h = "Ankit\fbook"

print(h) # returns 'book'

# 9. \v: Vertical tab
i = "Ankit\vbook"

print(i) # returns 'book'

# 10. \ooo: Octal value
j = "Ankit\123book"

print(j) # returns 'AnkitSbook'
