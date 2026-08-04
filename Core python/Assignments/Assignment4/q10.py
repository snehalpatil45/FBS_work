# write a program to check number is perfect or not.

num = int(input('Enter number:'))
sum = 0
for i in range(1,num):
    if(num % i == 0):
        sum += i
if(num == sum):
    print(f'{num} is a perfect number.')
else:
    print(f'{num} is not a perfect number.')