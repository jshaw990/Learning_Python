# for loops
# works with strings, integers, trupals, lists, sets

for item in 'Learning Python':
    print(item)

for item in [1,2,3,4,5]:
    print(item)

for item in (6,7,8,9,0):
    for x in ['a', 'b', 'c']:
        print(item, x)

# iterables
# iterated => one by one to check each item in the collection
# object or collection that can be iterated over
# list, dictionary, tuple, set, string
user = {
    'name': 'John',
    'age': 50,
    'logged_in': False
}

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

for key, value in user.items():
    print(key, value)