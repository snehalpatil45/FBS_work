# type 4 - with passing parameter (with input)
       # - with returning value (with output) 

def add(num1,num2):
    
    # sum = num1 + num2
    # return sum

    return num1 + num2

num1 = int(input('Enter number 1:'))
num2 = int(input('Enter number 2:'))

res = add(num1,num2)
print(f'Addition of {num1} and {num2} is {res}')
