#11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.
def armstrong(num):
    original = num
    s = 0

    while (num > 0):
        r = num % 10
        s = s + r**3
        num = num // 10

    if (s == original):
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

num = int(input("Enter number: "))
armstrong(num)