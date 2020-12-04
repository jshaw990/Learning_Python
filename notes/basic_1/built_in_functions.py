# built in functions

print(len('012345678')) # -> 9

greet = "hello"
print(greet[0:len(greet)])

# methods
# methods that can be used only on strings
# .format() # this is a method

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be')) # -> 3 finds index 
print(quote.replace('be', 'me')) # replaces word in string
print(quote) # prints inital string -- strings are immutable

quote2 = quote.replace('be', 'me') 
print(quote2) # prints replaced quote