#9. Write a program to check if entered number is a palindrome or
# not.
def palindrome(num):
    original = num
    rev = 0

    while (num > 0):
        r = num % 10
        rev = rev * 10 + r
        num = num // 10

    if (original == rev):
        print("Palindrome Number")
    else:
        print("Not Palindrome")

num = int(input("Enter number: "))
palindrome(num)