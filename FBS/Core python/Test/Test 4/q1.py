# 1. write a program to check stron number using function.

def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact 

def isStrong(num):
    temp = num
    sum = 0
    while(num > 0):
        digit = num % 10
        sum = sum + fact(digit)
        num = num // 10
    return temp == sum

num = int(input('Enter number:'))
if(isStrong(num)):
    print(f'{num} is strong number.')
else:
    print(f'{num} is not a strong number.')