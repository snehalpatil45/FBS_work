# write a program to check if given number is strong number.

num = int(input('Enter number:'))
sum = 0
for digit in str(num):
    fact = 1
    for i in range(1, int(digit)+1):
        fact = fact*i
    sum = sum + fact
if(sum == num):
    print(f'{num} is a strong number.')
else:
    print(f'{num} is not a strong number.')