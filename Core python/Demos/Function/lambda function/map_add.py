# method 1
num1 = [1,2,3,4]
num2 = [7,8,9,10]
res = list(map(lambda x,y : x + y ,num1,num2))
print(res)

# method 2
li = [(1,3),(2,4),(3,5)]
print(list(map(lambda x,y,z : x + y + z,num1,num2,num1)))