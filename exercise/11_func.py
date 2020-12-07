from functools import reduce 

# capitalize all of the names and print the list
my_pets = ['kimi', 'olive', 'ember', 'remy']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))

# zip the two lists into a list of tuples and sort highest to lowest
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

# filter the scores over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))

# combine all the numbers in a list (my_numbers and scores) 
# what is the total? 

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))