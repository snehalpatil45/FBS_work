# wap to input all sides of rectangle and check whether the rectangle is valid or not.

a = int(input('Enter side a:'))
b = int(input('Enter side b:'))
c = int(input('Enter side c:'))
d = int(input('Enter side d:'))
if( a == c and b == d ):
	print('Rectangle is valid')
else:
	print('Rectangle is invalid')