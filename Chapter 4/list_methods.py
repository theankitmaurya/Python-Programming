# List methods -> append, insert, remove, pop, clear, index, count, sort, reverse, copy


friends = ["Apple", "Banana", 5, 23.9, False, "Shubham", "Rohan"]
print(friends)

# 1. L1.append() -> adds an element at the end of the list
friends.append("Mango")
print(friends)

# 2. L1.insert() -> adds an element at the specified index
friends.insert(1, "Pineapple")
print(friends)

# 3. L1.remove() -> removes the first occurrence of the element
friends.remove("Banana")
print(friends)

# 4. L1.pop() -> removes the element at the specified index
friends.pop(2)
print(friends)

# 5. L1.index() -> returns the index of the first occurrence of the element
friends = ["Apple", "Banana", 5, 23.9, False, "Shubham", "Rohan"]
print(friends.index("Banana"))

# 6. L1.count() -> returns the number of occurrences of the element
print(friends.count("Banana"))

# 7. L1.sort() -> sorts the list in ascending order
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)

# 8. L1.reverse() -> reverses the list
friends.reverse()
print(friends)

# 9. L1.copy() -> returns a copy of the list
friends_copy = friends.copy()
print(friends_copy)

# 10. L1.clear() -> removes all the elements from the list
friends.clear()
print(friends)
