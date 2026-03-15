#5. Sum of all prime numbers between 1 to n
def is_prime(num):
    if (num < 2):
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_prime(n):
    s = 0
    for i in range(1, n+1):
        if (is_prime(i)):
            s = s + i
    return s

n = int(input("Enter n: "))
print(f'Sum of prime numbers :{sum_prime(n)}')