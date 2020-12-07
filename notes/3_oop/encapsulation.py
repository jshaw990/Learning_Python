# encapsulation
# the binding of data and functions that encapsulate the data
# data = attributes
# functions = methods

# in the following the PlayerCharacter class allows for 
# a more streamlined creation of a character rather than larger individual functions

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old!')

player1 = PlayerCharacter('John', 50)

print(player1.speak())