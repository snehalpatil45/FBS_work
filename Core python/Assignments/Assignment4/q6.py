# wap to check if given number is prime number or not.

num = int(input('Enter number:'))
i = 2
while(i <= num):
    if(num % i == 0):
        print(f'{num} is not a prime number.')
        break
    i = i + 1
else:
    print(f'{num} is a prime number.')