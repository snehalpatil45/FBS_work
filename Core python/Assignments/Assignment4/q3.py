# write a program to print sum of series upto n

n = int(input('Enter number:'))
i = 1
sum = 0
while(i <= n ):
	sum += i
	i = i + 1
	print('sum:',sum)