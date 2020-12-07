# comprehensions 
# list comprehensions
# set comprehensions
# dictionary comprehensions 

# quick way to create lists, sets, or dictionarys without 
# having to loop or append

# list comprehensions 
my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num for num in range(0,100)]
print(my_list2)

my_list3 = [num**2 for num in range(0,100)]
print(my_list3)

my_list4 = [num**2 for num in range(0,100) if num % 2 ==0]
print(my_list4)

# set comprehensions
my_set = {char for char in 'hello'}
print(my_set)

my_set2 = {num for num in range(0,100)}
print(my_set2)

my_set3 = {num**2 for num in range(0,100)}
print(my_set3)

my_set4 = {num**2 for num in range(0,100) if num % 2 ==0}
print(my_set4)

# dictionary comprehensions
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0} 
print(my_dict)

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)