# write a program to print first n prime numbers

n = int(input('Enter value of n:'))
num = 1
prime_count = 0
while(prime_count < n):
    num = num + 1
    count = 0
    for i in range(1,num+1):
        if(num%i == 0):
            count= count + 1
    if (count == 2):
        print(num)
        prime_count = prime_count + 1