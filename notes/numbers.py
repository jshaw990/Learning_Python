# int & float

print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)

print(type(2 + 4)) # -> class 'int
print(type(2 - 4)) # -> class 'int
print(type(2 * 4)) # -> class 'int
print(type(2 / 4)) # -> float 
print(type(9.9 + 1.1)) # -> float 

# floats use up more space than int in memory

print(2 ** 2) # to the power of
print(2 // 4 ) # rounded to nearst int
print(5 % 4) # modulo - remainder of 

# math functions 
print(round(3.1))
print(abs(-20)) # absolute values

# operator precedence ie. BEDMAS () ** / * + -
print(20 - 3 * 4) # -> 8

print(bin(5)) # -> 0b101
print(int('0b101', 2)) # -> 5