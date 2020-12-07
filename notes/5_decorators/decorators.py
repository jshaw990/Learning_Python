# decorators 
# @classmethod and @staticmethod are decorators
# higher order function (HOC) is any function that 
# accepts a function as a parameter or that returns a function
# decorators are functions that wrap another function and enhances it

def my_deco(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_func 

@my_deco
def hello():
    print('hello')

hello()

### 

from time import time 

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} seconds to compute')
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5

long_time()