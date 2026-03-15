#4. Sum of all odd numbers between 1 to n
def sum_odd(n):
    s = 0
    for i in range(1, n+1):
        if (i % 2 != 0):
            s = s + i
    return s

n = int(input('Enter n: '))
print(f'Sum of odd numbers :{sum_odd(n)}')