x = 10
y = 10
z = 20
li1 = [ 10,20,30 ]
li2 = [ 10,20,30 ]
# 1. is
print( x is y )
print( x is z)
print( li1 is li2)
print(id(x))
print(id(y))
print(id(z))
print(id(li1))
print(id(li2))
print(id(li1[0]))