# default parameter
# 1.to make parameter optional(can or can't pass value to this parameter)
# 2. assigning value to parameter in function defination.
# 3.if we pass value to default parameter ,it take passed value
  # if we dont pass value it takes default value
# flow of assigning default value is right to left

def add(num1, num2,num3,num4=0):
    print(num1+num2+num3+num4)
add(10,20,30)