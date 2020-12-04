# list 
# collection of items
# similar to arrays

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# data structures
# ways of organizing data 

cart = ['notebook', 'pencil', 'ruler']
print(cart[1]) # -> pencil
# print(cart[3]) # invalid -> out of range

# list slicing
cart_2 = [
    'notebook',
    'pencil',
    'ruler',
    'calculator',
    'pen',
    'mousepad'
    ]

print(cart_2) # prints whole cart
print(cart_2[0::2]) # steps over second item

# lists are mutable 
cart_2[0] = 'laptop' # replaces notebook with laptop
print(cart_2)
