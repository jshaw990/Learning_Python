# dummy import example
# import statement does not require .py extension
# a folder containing modules is called a package
# the files in the folder are called modules

# imported as module
import utility 

# imported as package.module
import ex_folder.multiply

# another way to write this is
# import * will import all functions 
# from ex_folder.multiply import * 

# utilized as module.function
print(utility.addition(2,3))

print(utility.subtraction(2,3))

# utilized as package.module.function
print(ex_folder.multiply.multiply(2,3))

# package may be assigned as a variable for QOL
multi = ex_folder.multiply.multiply 

print(multi(3,6))

# individual functions may be imported from a package
from ex_folder.multiply import divide 

# multiple functions may be imported from one package in one line
from ex_folder.multiply import multiply, divide 

# the imported function is written as if it is based in this module
print(divide(3,6))

if __name__ == '__main__':
    print('You are running the main')