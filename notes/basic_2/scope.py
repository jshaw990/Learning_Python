# scope
# what variables do we have access to 

a = 1

def my_func():
    a = 5 
    return a

print(a) # -> 1 
print(my_func()) # -> 5 scope of a = 5 is limited to my_func 
print(a) # -> 1 scope is still limited

# order of scope: 
# 1 - local scope
# 2 - parent scope
# 3 - global scope
# 4 - built in python function

# global variables
total = 0

def count():
    global total # global keyword will use global variable
    total += 1 
    return total 

print(count())

# this also injects the global variable

def count1(total):
    total += 1
    return total 

print(count1(total))