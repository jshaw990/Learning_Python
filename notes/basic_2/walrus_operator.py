# walrus operator
# := 
# assigns values to variables as part 
# of a larger expression

a = 'hello'

if (len(a) > 4):
    print(f'too long {len(a)} elements')

# using the walrus operator
if ((n := len(a)) > 4): 
    print(f'too long {n} elements')

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)