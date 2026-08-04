#8. Write a program find reverse of a number
def reverse_number(num):
    rev = 0
    while (num > 0):
        r = num % 10
        rev = rev * 10 + r
        num = num // 10
    return rev

num = int(input("Enter number: "))
print(f'Reverse : {reverse_number(num)}')