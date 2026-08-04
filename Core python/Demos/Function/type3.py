# type 3 - without passing parameter (without input)
       # - with returning value (with output) 

def add():
    num1 = int(input('Enter number 1:'))
    num2 = int(input('Enter number 2:'))

    sum = num1 + num2

    return sum

res = add()
print('addition:',res)