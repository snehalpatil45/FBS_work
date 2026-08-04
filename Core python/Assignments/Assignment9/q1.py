# write a program to find sum of following series using recursive function.
# 1! + 2! + 3! +....+n!

def fact(n):
    if (n == 0 or n == 1):
        return 1
    return n * fact(n - 1)

def sumofseries(n):
    if(n == 1):
        return 1
    return fact(n) + sumofseries(n - 1)

n = int(input('Enter number:'))
print(f'sum: {sumofseries(n)}')