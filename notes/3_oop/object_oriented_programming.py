# object oriented programming
# everything in python is an object
# we are able to create our own data types with methods 
# everything in python is a class 
# classes are written in CamelCase
# classes allow us to instantiate different objects using the same blueprint

# four main pillars of OOP
# abscration
# encapsulation
# inheritance 
# polymorphism

class BigObject: 
    pass

obj = BigObject() # instantiate

class PlayerCharacter:
    membership = True                           # class object attribute static not dynamic
    def __init__(self, name='anon', age=0):     # self creates dynamic object 
        if (age > 18):
            self.name = name                    # constructor method
            self.age = age
            print(f'{self.name} has been successfully initialized!')
        else: 
            self.name = name 
            self.age = age 
            print(f'{self.name} is only {self.age} years old and cannot join the game...') 

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod 
    def adding_things(cls, num1, num2):
        return cls('Frank', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2
    
    def run(self):
        print(f'{self.name} is running')

player1 = PlayerCharacter('John', 44) 
player2 = PlayerCharacter('Tom', 21)
player3 = PlayerCharacter('James', 10)
player4 = PlayerCharacter.adding_things(2,3)

print(player1.shout())
print(player1.run())
print(player2.shout())
# help(player1) will print the blueprint in console 