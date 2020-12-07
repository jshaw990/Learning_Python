# method resolution order
# rule that python follows for when a method
#       A
#      / \
#    /   \
#   B    C
#   \   /
#   \  /
#    D

class A: 
    num = 10

class B(A):
    pass

class C(A):
    num = 1 

class D(B, C):
    pass 

print(D.num) # calculates based off MRO: D > B > C > A 
print(D.mro()) # Prints out order of operations