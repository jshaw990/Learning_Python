# tuple
# similar to lists but immutable
# usually faster than lists 
# safer than lists as they cannot change

my_tuple = (1,2,3,4,5)

print(my_tuple[2]) # can grab item
print(5 in my_tuple) # can find item

new_tuple = my_tuple[1:2]
print(new_tuple)

# count

print(my_tuple.count(5))

# index

print(my_tuple.index(4))

# length
print(len(my_tuple))

