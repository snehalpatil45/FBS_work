# type 2 - with passing parameter (with input)
       # - without returning value (without output) 

def addition(num1,num2):

    sum = num1 + num2
    print(f'Addition of {num1} and {num2} is {sum}')

num1 = int(input('Enter number 1:'))
num2 = int(input('Enter number 2:'))
addition(num1,num2)