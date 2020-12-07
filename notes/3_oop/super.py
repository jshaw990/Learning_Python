# super()
# super allows us to pass the inherited classes init values to subclasses

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

class Wizard(User):     # adding User to the class passes the functions down
    def __init__(self, name, power, email):
        super().__init__(email)     # super() allows us to run the User without refering to self
        self.name = name
        self.power = power 

    def attack(self):
        print(f'{self.name} is Attacking with {self.power}')

class Archer(User):     # these may be called sub classes
    def __init__(self, name, num_arrow, email):
        User.__init__(self, email)  # if we do not use super() 
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f'{self.name} is Attacking with arrows: remaining: {self.num_arrow}')

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100, 'robin@gmail.com')

print(wizard1.email)