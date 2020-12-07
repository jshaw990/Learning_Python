# introspection
# ability to determine the type of the object at the runtime
# allows us to examine the code as it is running

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

class Wizard(User):     
    def __init__(self, name, power, email):
        super().__init__(email)     
        self.name = name
        self.power = power 

    def attack(self):
        print(f'{self.name} is Attacking with {self.power}')

class Archer(User):    
    def __init__(self, name, num_arrow, email):
        super().__init__(email)  
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f'{self.name} is Attacking with arrows: remaining: {self.num_arrow}')

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100, 'robin@gmail.com')

print(wizard1.email)

print(dir(wizard1)) # allows us to view all the functions associated with the class
