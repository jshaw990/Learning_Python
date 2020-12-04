# functions
# def initiates or defines a function

def say_hello():
    print('hello')

# below calls or invokes the function to run
say_hello()

# parameters 
def say_hi(name, emoji):
    print(f'Hello {name} {emoji}')

# arguments passed to function parameters
# these are positional
say_hi('Jayden', ':)')

# keyword arguments
say_hi(emoji=':)', name='John')

# default parameters
def say_hola(name='Jim', emoji='B)'):
    print(f'Hello {name} {emoji}')

say_hola()