#keyword variable length
#1. to pass multiple values with attribute name
#(to understand meaning of value)
#2.mention two *(asterisk) before parameter name in function defination
#3. store values and attribute name in dictionary format.
#4. use for loop to iterate items from dict.items()

def emp(**data):
    #print(data)
    for key,val in data.items():
        print(f'{key}:{val}')
emp(id = 101,name='abc',sal = 35000)