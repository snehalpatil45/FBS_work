# write a program to check if given number is armstrong or not.

num = int(input('Enter number:'))
sum = 0
count = len(str(num))
for digit in str(num):
    sum = sum + int(digit)**count
if(sum == num):
    print(f'{num} is armstrong number.')
else:
    print(f'{num} is not armstrong number.')