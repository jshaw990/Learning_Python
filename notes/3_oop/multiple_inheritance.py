# multiple inheritance

class User():
    def sign_in(self):
        print('Logged in')

class Wizard(User):     # adding User to the class passes the functions down
    def __init__(self, name, power):
        self.name = name
        self.power = power 

    def attack(self):
        print(f'{self.name} is Attacking with a power of {self.power}')

class Archer(User):     # these may be called sub classes
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def check_arrows(self):
        print(f'{self.name} has {self.num_arrow} arrows remaining')

class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
hybrid1 = Hybrid('Hybrid', 30, 80)

print(hybrid1.attack())