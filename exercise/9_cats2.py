class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is walking around'

class Ember(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Remy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Olive(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats = [Ember('Ember', 3), Remy('Remy', 1), Olive('Olive', 4)]

my_pets = Pets(my_cats)

my_pets.walk()