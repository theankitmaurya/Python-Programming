# Write a python function to remove a given word from a list and strip it at the same time.

l = ["Ankit", "Rohan", "Shubham", "Divya"]

def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

print(remove(l, "an"))
