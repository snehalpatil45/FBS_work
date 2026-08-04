import functools

data = [1,2,3,4,5,6,7,8,9,10]
print(functools.reduce(lambda x,y : x + y ,data))

#from functools import reduce
#data = [1,2,3,4,5,6,7,8,9,10]
#res = reduce(lambda num1,num2 : num1 + num2, data)
#print(res)

# operation
#num1   num2
#       + 1    = 1
#   1   + 2    = 3
#   3   + 3    = 6

# and so on