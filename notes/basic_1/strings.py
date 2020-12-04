# strings - str
# can be written with ' ' or " "

print(type('Hello there')) # -> <class 'str'>

username = 'user100'
password = '1234'

# multiline strings
long_string = ''' 
wow 
hello
---
'''

print(long_string)

first_name = 'Jayden'
last_name = 'Shaw'
full_name = first_name + ' ' + last_name
print(full_name)

# string concatenation
# adding strings together
print('hello' + first_name)

# formatted strings

name = 'John'
age = 55
print('Hi ' + name + '. You are ' + str(age) + ' years old')

# python3
print(f'Hi {name}. You are {age} years old') # f at start indicates formatted string

# python2
print('hi {}. You are {} years old.'.format(name, age))
print('hi {1}. You are {0} years old.'.format(name, age))

# string index 
# str is an ordered sequence of characters
# 
selfish = 'me me me'
print(selfish)
print(selfish[0]) # -> m // grabs letter at index 0

# when using [] = start
# [start:stop]

print(selfish[0:2]) # -> me

# [start:stop:stepover]
print(selfish[0:8:2]) # -> m em 
print(selfish[-1]) # -> e starts at the last character
print(selfish[::-1]) # reverses order

# immutability
# strings can be reassigned
# strings cannot be immutable 
string_1 = '01234567'
string_1 = '8' # valid

# string_1[0] = 8 # not valid