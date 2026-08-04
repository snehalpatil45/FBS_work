def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def is_strong(num):
    temp = num
    sum = 0
    while(num>0):
        digit = num % 10
        sum = sum + factorial(digit)
        num = num // 10
    return temp==sum
n = int(input('Enter number:'))
if(is_strong(n)):
    print('strong number')
else:
    print('not strong number')