# sum of digits 

def sumofdigits(n):
    if(n == 0):
        return 0
    return n % 10 + sumofdigits(n // 10)

num = int(input('Enter number:'))
print(f'sum of digits : {sumofdigits(num)}')