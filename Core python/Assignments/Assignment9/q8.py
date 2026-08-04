# prime number

def is_prime(n , i = 2):
    if(n <= 1):
        return False 
    if(n == 2):
        return True
    if(n % i == 0):
        return False
    if(i * i > n):
        return True
    return is_prime(n,i+1)

num = int(input('Enter number:'))
if (is_prime(num)):
    print('prime number')
else:
    print('not prime')