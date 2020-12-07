class Cat: 
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age 

cat1 = Cat('Ember', 2)
cat2 = Cat('Olive', 4)
cat3 = Cat('Remy', 1)

def get_oldest_cat(*args):
    return max(args)

print(f'The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old')

print(cat1.name)
print(cat2.name)
print(cat3.name)