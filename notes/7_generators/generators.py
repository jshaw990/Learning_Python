# generators 
# allow us to generate a sequence of values over time
# ex. range()
# generators allow us to complete operations without holding values in memory

def generator_function(num):
    for i in range(num):
        yield i * 2        # yield pauses the function and continues with next

gen = generator_function(100)
next(gen)   # runs another iteration of generator_function
next(gen)
next(gen)
print(next(gen))