# write a program to print factorial of a number.

n = int(input('Enter number:'))
fact = 1
i = 1
while(i <= n ):
	fact *= i
	i += 1
	print('factorial:', fact )