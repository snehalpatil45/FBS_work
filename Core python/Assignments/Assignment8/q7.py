# 7. Write a program to find sum of digits of a number.
def sum_digits(num):
    s = 0
    while (num > 0):
        r = num % 10
        s = s + r
        num = num // 10
    return s

num = int(input("Enter number: "))
print(f'Sum of digits : {sum_digits(num)}')