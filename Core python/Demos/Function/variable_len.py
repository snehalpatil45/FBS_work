# variable length argument/parameter
#1. to pass multiple values to function
#2.mention *(asterisk) before parameter name in function defination.
#3.store all passed values in tuple.

def add(*numbers):
    #print(type(numbers))
    sum = 0
    for num in numbers:
        sum += num
    return sum
    
res = add(10,20,30,40)
print(res)