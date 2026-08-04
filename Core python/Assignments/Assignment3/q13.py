# write a program to input electricity unit charges and calculate total electricity bill accordingly to the given condition: 1.for first 50 units rs 0.50/unit
#2. for next 100 units rs 0.75/unit  3.for next 100 units rs 0.75/unit  3.for next 100 units rs 1.20/unit  4. for unit above 250 rs 1.50/unit.
# an additional subcharge of 20 % is added to the bill.


units = int(input('Enter units consumed:'))
bill = 0
if(units <= 50):
	bill = units * 0.50
elif(units <= 150):
	bill = (50 * 0.50) + (units - 50) * 0.75
elif(units <= 250):
	bill = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20
else:
	bill = (50 * 0.50) + (100 * 0.75) + ( 100 * 1.20) + (units - 250) * 1.50
bill = bill + ( bill * 0.20)
print('Total bill:',bill)