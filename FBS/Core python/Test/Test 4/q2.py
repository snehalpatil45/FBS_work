# write a program to check palindrome

def Palindrome(num):
    original = num
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = rev*10 + rem 
        num = num // 10
    if(original == rev):
        print(f'{original} is palindrome number.')
    else:
        print(f'{original} is not a palindrome number.')

num = int(input('Enter number:'))
Palindrome(num)