num = int(input('Enter number:'))
sum = 0
while(num > 0):
    sum = sum+ num%10
    num = num // 10
print('sum of digit of number is',sum)