# Sets

my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#Union - it combines two sets into one and remove duplicate data
uni_set = set1.union(set2)
print(uni_set)

#Intersection - prints out common data between the two sets
inter_set = set1.intersection(set2)
print(inter_set)

#Difference - prints out data from a set1 that is not in set2
diff_set = set1.difference(set2)
print(diff_set)