# while loop

i = 0 

while i < 10:
    print(i)
    # i = i + 1
    i += 1 # both options work
else: 
    print('while loop completed')

# if a break statement is present
# else will not be executed

while True: 
    response = input('Enter text: ')
    if (response == 'bye'):
        break

# break exits from current loop
# continue will go back to the top of current loop
# pass will continue to the next line 
# -- usually used as placeholder during development
