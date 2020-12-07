# set
# unordered collection of unique objects
# sets do not have an index

my_set = {1,2,3,4,5}

print(my_set)

my_set_2 = {1,2,3,4,5,5,4,3,2,1}
print(my_set_2) # -> {1,2,3,4,5} only shows unique values
print(len(my_set_2)) # does not include number of non-unique values

my_list = [1,2,3,4,5,5]

print(set(my_list)) 

# methods

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9,0}

# .difference

print(set1.difference(set2)) # -> 1,2,3 displays different items between sets

# .discard

print(set1.discard(5))
print(set1)

# .difference_update

print(set1.difference_update(set2))
print(set1)

# .intersection

print(set1.intersection(set2))
print(set1 & set2) # this does the same

# .isdisjoint
print(set1.isdisjoint(set2))

# .issubset
print(set1.issubset(set2))

# .issuperset
print(set1.issuperset(set2))

# .isunion - combines set and removes duplicates
print(set1.union(set2))
print(set1 | set2) # this does the same