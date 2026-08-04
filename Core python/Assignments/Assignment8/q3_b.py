# b. 1!+ 2! + 3! + 4!+..... + n!
def factorial(x):
    f = 1
    for i in range(1, x+1):
        f = f * i
    return f

def sum_factorial(n):
    s = 0
    for i in range(1, n+1):
        s = s + factorial(i)
    return s

n = int(input('Enter n: '))
print(f'Sum of factorial series :{sum_factorial(n)}')