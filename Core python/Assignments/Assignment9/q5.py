# write a program to find factorial using recursion.

def factorial(n):
    if(n > 0):
        return n * factorial(n-1)
    elif(n == 0):
        return 1
    else:
        return None
    
n = int(input('Enter number:'))
res = factorial(n)
print(f'factorial of {n} is {res}')