# dunder methods
# python specific methods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'John',
            'is_active': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self): 
        return 5

    def __call__(self):
        print('CALLED')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(len(action_figure))
print(action_figure['name'])