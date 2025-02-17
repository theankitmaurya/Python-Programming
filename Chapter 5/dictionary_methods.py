marks = {
    "John": 90,
    "Ankit": 100,
    "Raj": 80,
    "list": [1, 2, 3]
}

print(marks.items()) # returns dict_items([('John', 90), ('Ankit', 100), ('Raj', 80), ('list', [1, 2, 3])])
print(marks.keys()) # returns dict_keys(['John', 'Ankit', 'Raj', 'list'])
print(marks.values()) # returns dict_values([90, 100, 80, [1, 2, 3]])

marks.update({"John": 95, "Shubham": 90})
print(marks) # returns {'John': 95, 'Ankit': 100, 'Raj': 80, 'list': [1, 2, 3], 'Shubham': 90}

print(marks.get("Ankit")) # returns 100
print(marks.get("Ankit1")) # returns None
print(marks["Ankit2"]) # returns KeyError: 'Ankit2'
