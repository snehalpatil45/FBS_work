# write a program to print all numbers in a range divisible by a given number.

num = int(input('Enter number:'))
d = int(input('Enter divisor:'))
for i in range(1,num + 1):
    if(i % d == 0):
        print(i)