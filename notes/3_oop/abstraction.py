# abstraction
# hiding of information and giving access to only what is necessary

# in the following, player1 is only given access to the speak function
# this abstracts the remaining data

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