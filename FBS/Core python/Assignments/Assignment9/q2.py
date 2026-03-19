# write a program to check if given nummber is armstrong or not using recursive function.

def power(x,y):
    if(y == 0):
        return 1
    return x * power(x,y-1)

def armstrong(n,digits):
    if(n == 0):
        return 0
    return power(n % 10 , digits) + armstrong(n // 10,digits)

num = int(input('Enter number:'))
digits = len(str(num))
if (armstrong(num,digits) == num):
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not armstrong number')