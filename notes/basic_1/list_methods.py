# list methods

basket = [1,2,3,4,5]
print(len(basket)) # -> 5

# adding | append
new_basket = basket.append(100)
newer_basket = basket

print(basket)
print(new_basket)
print(newer_basket)

basket.insert(4, 50) # inserts 50 in index 4 of basket
print(basket)
# -> [1, 2, 3, 4, 50, 5, 100]

# removing
basket.pop() # removes last index item
basket.pop(0) # removes item at index 0
print(basket)

basket.remove(4) # removes number 4 regardless of index
print(basket)

basket.clear() # completely clears list of items
print(basket)

# indexing 
basket_2 = ['a','b','c','d','e']
print(basket_2.index('d')) # -> 3 returns index of string
# print(basket_2.index['d', 0, 4]) # returns nothing, index stops before string

# python keywords
print('d' in basket_2) # -> true
print('x' in basket_2) # -> false letter is not there
print(basket_2.count('d')) # -> 1 counts how many times value is in list

basket_3 = ['a','b','c','d','c','d','e','f']
basket_3.sort() # sorts list alphabetically
print(basket_3)

print(sorted(basket_3))

basket_3.reverse()
print(basket_3) # reverses basket

basket_4 = ['a','b','c','d','c','d','e','f']
basket_4.sort()
print(basket_4[::-1])

# generate range
# range(start int, stop int)

print(list(range(1,100))) # -> 1, 2, 3, ..... 97, 98, 99 

# .join 
sentence = ' '
sentence.join(['hello', 'my', 'name', 'is', 'Jayden'])

new_sentence = sentence.join(['hello', 'my', 'name', 'is', 'Jayden'])
print(new_sentence)

new_sentence2 = ' '.join(['hello', 'my', 'name', 'is', 'Jayden'])
print(new_sentence2)

# list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)
