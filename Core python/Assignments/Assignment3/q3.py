# wap to input angles of a triangle and check whether triangle is valid or not.

a = int(input('Enter angle a:'))
b = int(input('Enter angle b:'))
c = int(input('Enter angle c:'))
total = a + b + c
if ( total == 180 ):
	print('Triangle is valid')
else:
	print('Triangle is invalid')