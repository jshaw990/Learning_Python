# random is a built in python module
# choice is the function within the module

import random 

choice = random.choice([1,2,3,4,5,6])

print(f'Random number = {choice}')

# sys
# 

import sys 

first = sys.argv[1]
last = sys.argv[2]

print(f'Hello {first} {last} ')