# write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter a 3 digit number:'))
a = num // 100
b = num % 10
if(a == b):
	print('Number is palindrome')
else:
	print('Number is not palindrome')