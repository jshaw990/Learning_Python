# functional programming
# emphasis on simplicity where data and functions are concerned 
# the main concept is pure functions 

# pure functions

# two rules
# 1. given the same input it will always output the same result
# 2. a function should not produce any side effects [ie. printing]

def multiply_by2(li):
    new_list = []
    for item in li: 
        new_list.append(item * 2)
    # return print(new_list) <- this is a side effect and breaks the rules
    return new_list

print(multiply_by2([1,2,3]))

# pure functions allow for cleaner, less buggy code
# it is almost impossible to create a program without creating non pure functions