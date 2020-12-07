# common functions
# map
    # make an itterator that computes the function 
    # using arguments from each of the iterables

my_list = [1,2,3]
your_list = [10,20,3,]

def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, my_list)))

# filter
    # Return an iterator yielding those items of iterable 
    # for which function(item) is true

def only_odd(item):
    return item % 2 != 0
    
print(list(filter(only_odd, my_list)))

# zip
    # takes two (or more) iterables 
    # grabs first item of each and zips them together
    # very generic
    # can be used in a lot of ways to create new data structures

print(list(zip(my_list, your_list)))

# reduce 
    # not a built in python function
    # must be imported from functools
    # 

from functools import reduce # initial import

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator , my_list, 0))