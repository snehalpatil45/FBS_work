# wap to check whether the triangle is equilateral ,isosceles or scalene triangle.

a = int(input('Enter side a:'))
b = int(input('Enter side b:'))
c = int(input('Enter side c:'))
total = a + b + c
if( total == 180):
	if( a == b == c):
		print('It is equilateral triangle')
	elif( a == b or b == c or a == c):
		print('It is isosceles trianle')
	else:
		print('It is scalene triangle')
else:
	print('Triangle is invalid')