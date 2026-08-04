# type 1 - without passing parameter (without input)
       # - without returning value (without output) 

def addition():
    num1 = int(input('Enter number 1:'))
    num2 = int(input('Enter number 2:'))

    sum = num1 + num2
    print(f'Addition of {num1} and {num2} is {sum}')

addition()