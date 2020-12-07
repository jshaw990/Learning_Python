# private vs public variables
# in python there is not true private variable
# adding an underscore denotes to programmers a private variable
# this is a programmer convention and not a python rule

class PlayerCharacter:
    def __init__(self, name, age): # __init (double underscore) is a dunder method
        self._name = name   # _name should not be modified
        self._age = age     # _age should not be modified
    
    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old!')

player1 = PlayerCharacter('John', 50)

print(player1.speak())