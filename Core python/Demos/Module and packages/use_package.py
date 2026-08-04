# method 1
# from my_package import module
# print(module.addition(10,20))

# method 2
# from my_package.module import *
# print(addition(10,20))

# method 3
# from my_package.module import multiplication
# print(multiplication(3,4))

# method 4
from my_package.module import multiplication as mult
print(mult(234,32423))