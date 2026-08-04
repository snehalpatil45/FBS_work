# write a program to find sum of n numbers using recursion.

def sumofseries(n):
    if( n > 0):
        return n + sumofseries(n - 1)
    elif(n == 0):
        return 0
    else:
        return None
    
n = int(input('Enter number:'))
res = sumofseries(n)
print(f'sum of n numbers is {res}')