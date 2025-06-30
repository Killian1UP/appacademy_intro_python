
fruits = ["apple", "banana", "cherry"]

# print(fruits[0])    # prints out a single parameter of your choice through indexing

# fruits[1] = "blueberry"   # replace a parameter with a new one

# print(fruits)

fruits.append("Kiwi")    # adds a parameter on the list
print(fruits)

fruits.insert(1, "orange")    # adds a parameter at a specific index of your choice
print(fruits)

fruits.remove("Kiwi")    # removes a specific parameter in the list
print(fruits)

fruits.sort()        # sorts the list in ascending order
print(fruits)

fruits.sort(reverse=True)     # sorts the list in decending order
print(fruits)