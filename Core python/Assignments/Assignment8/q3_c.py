# c. 1^1 + 2^2 + 3^3+ ...... n^n
def power_series(n):
    s = 0
    for i in range(1, n+1):
        s = s + (i ** i)
    return s

n = int(input("Enter n: "))
print(f'Sum : {power_series(n)}')