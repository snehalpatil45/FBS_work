x = 10
y = 20

# method 1
# import my_module
# print(my_module.addition(x,y))

# method 2
# from my_module import * 
# print(addition(x,y))

# method 3
# from my_module import addition,subtraction
# print(addition(x,y))
# print(subtraction(y,x))

# method 4
from my_module import addition as add
print(add(x,y))