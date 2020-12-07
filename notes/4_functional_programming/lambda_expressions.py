# lambda expressions/functions
# one time annonymous functions that are not needed more than once
# once run it is removed from the computer's memory 

# written as:
# lambda param: action(param)

from functools import reduce

my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list))