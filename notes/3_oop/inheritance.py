# inheritance
# allows new objects to inherit the properties of existing objects

# below, Users will be assigned a different player class (wizard or archer)
# but they must be logged in and require access to sign_in function 

class User():
    def sign_in(self):
        print('Logged in')

class Wizard(User):     # adding User to the class passes the functions down
    def __init__(self, name, power):
        self.name = name
        self.power = power 

    def attack(self):
        print(f'{self.name} is Attacking with {self.power}')

class Archer(User):     # these may be called sub classes
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f'{self.name} is Attacking with arrows: remaining: {self.num_arrow}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

# isinstance will allow us to check if a class is a subclass of another 
print(isinstance(wizard1, Wizard))  # -> True
print(isinstance(wizard1, User))    # -> True