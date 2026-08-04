# wap to calculate profit or loss.

cost_p = int(input('Enter cost price :'))
selling_p =  int(input('Enter selling price:'))
if( selling_p > cost_p ):
	print('It is a profit')
else:
	print('It is a loss')