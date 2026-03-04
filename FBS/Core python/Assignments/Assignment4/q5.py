# write a program to print Fibonacci series up to n.

n = int(input('Enter number:'))
a = -1
b = 1
c = a + b
while( c <= n ):
	print( c, end = ' ')
	a = b
	b = c
	c = a + b