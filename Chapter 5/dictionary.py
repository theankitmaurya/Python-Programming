# Properties of Python Dictionary ->
# 1. Dictionaries are mutable
# 2. Dictionaries are unordered
# 3. Dictionary keys are unique i.e. cannot contain duplicate keys
# 4. Dictionary are indexed by keys.

marks = {
    "John": 90,
    "Ankit": 100,
    "Raj": 80,
    "list": [1, 2, 3]
}

print(marks, type(marks)) # returns {'John': 90, 'Ankit': 100, 'Raj': 80} <class 'dict'>

print(marks["John"]) # returns 90

