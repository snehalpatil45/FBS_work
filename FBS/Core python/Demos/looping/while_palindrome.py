# write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter a 3 digit number:'))
original = num
reverse = 0
while(num > 0):
	digit = num % 10
	reverse = reverse * 10 + digit
	num = num // 10
if(original == reverse):
	print('Number is palindrome')
else:
	print('Number is not palindrome')