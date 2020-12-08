while True: 
    try:    # attempt to run this code
        age = int(input('How old are you? \n'))
        print(f'You are {age} years old')
    except ValueError: # if an error occurs in the try block, do this
        print('Please enter a number')
        continue # will return to the top of the loop
    except ZeroDivisionError: # specific error dependant
        print('Please enter a value above 0')
    else:   # break out of loop if try is accepted
        print('Thank you')
    finally: # runs regardless of errors 
        print('Operation Completed')