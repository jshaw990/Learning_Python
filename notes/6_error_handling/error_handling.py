# error handling

# errors in python
# an error that crashes a program is called an exception
# SyntaxError denotes a non standard python syntax error
# NameError denotes a name or variable that is undefined
# IndexError indicates an index is nonexistant 
# KeyError indicates a key in a dictionary that does not exist
# ZeroDivisionError shows when you attempt to divide by zero

# error handling in python
  
while True: 
    try:    # attempt to run this code
        age = int(input('How old are you? \n'))
        print(f'You are {age} years old')
            # raise ValueError('An error has occured') # will allow python error to display | will need to remove the ValueError except block
    except ValueError: # if an error occurs in the try block, do this
        print('Please enter a number')
        continue
    except ZeroDivisionError: # specific error dependant
        print('Please enter a value above 0')
        break
    else:   # break out of loop if try is accepted
        print('Thank you')

def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err: # combining and displaying errors
        print(f'Something went wrong...\nError: {err}')

print(sum('1', 2))