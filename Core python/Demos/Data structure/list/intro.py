# 1. structure: []
li = [10,20,30,40]
print(type(li))

#2. type of data: hetrogenous
li = [10,3.14,'snehal']
print(li)

# 3. sequence: ordered

# 4. changable : mutable
print(id(li))
li[0] = 50
print(id(li))
print(li)

# 5. Duplication : Allowed 
li = [10,20,10,10,30,20]
print(li)