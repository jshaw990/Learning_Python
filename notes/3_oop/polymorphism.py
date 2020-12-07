# polymorphism
# means 'many forms'
# refers to the way object classes have many names

# attack is shared, but the method calling it is different

class User():
    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do nothing')

class Wizard(User):     
    def __init__(self, name, power):
        self.name = name
        self.power = power 

    def attack(self):
        User.attack(self)
        print(f'{self.name} is Attacking with {self.power}')

class Archer(User):     
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        User.attack(self)
        print(f'{self.name} is Attacking with arrows: remaining: {self.num_arrow}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

# demo
# the same function is used for both archer and wizrd to attack
# but the result is different based on character type
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()