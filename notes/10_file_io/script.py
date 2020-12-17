# my_file = open('test.txt')

# print(my_file.readlines())

# my_file.close()

#with open('notes/10_file_io/test.txt') as my_file: 
#    print(my_file.read())

#with open('notes/10_file_io/test.txt', mode='r+') as my_file: 
#    text = my_file.write('Hello it\'s me!')

#with open('notes/10_file_io/test.txt', mode='a') as my_file: 
#    text = my_file.write('How are you??')

try: 
    with open('notes/10_file_io/test.txt') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
        print('That file does not exist')
        raise err