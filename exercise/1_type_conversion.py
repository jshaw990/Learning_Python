# type conversion

name = input('What is your name?\n')

birth_year = input('What year were you born?\n') 

current_year = 2020

age = current_year - int(birth_year) # convert input string to interger

print(f'{name}, you are {age} years old')