#3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
def sum_series(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

n = int(input('Enter n: '))
print(f'sum : {sum_series(n)}')