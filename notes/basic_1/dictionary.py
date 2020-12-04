# dictionary
# dict 
# dictionary = {
#   'KEY': VALUE,
#   'KEY': VALUE
# }
# dictionary keys may be expressed as int str bool 
# they must be immutable 
# keys must be unique
# if keys are not unique, the latter value will override 

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(dictionary['b']) # prints VALUE at KEY b

dictionary_2 = {
    'a': [1,2,3],
    'b': 'hello',
    'c': True
} # valid syntax

dictionary_3 = [
    {
        'a': [1,2,3],
        'b': 'hello',
        'c': True
    },
    {
        'a': [4,5,6],
        'b': 'goodbye',
        'c': False
    }
]
print(dictionary_3[0]['a'][1])

user = {
    'name': 'John',
    'location': 'Canada'
}

print(user.get('age')) # -> none no value is assigned
print(user.get('age', 30)) # -> 30 will assign value if not found

# another way to create dictionaries 
user_2 = dict(name='Kevin')
print(user_2)

# in
print('name' in user) # -> true

print('Canada' in user.keys()) # -> false
print('Canada' in user.values()) # -> true
print(user.items())

user_3 = user.copy() # copies user dictionary

print(user.clear()) # removes dictionary
print(user_3)

print(user_3.pop('location'))
print(user_3.popitem())
print(user_3)

print(user_3.update({'age': 50}))
print(user_3)