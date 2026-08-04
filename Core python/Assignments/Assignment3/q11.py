# accept age of 5 pepole and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition:
# 1. children below 12  = 30 % discount  2. senior citizen (above 59) = 50 % discount  3. other need to pay full.

total_amount = 0
age1 = int(input('Enter age of person 1:'))
ticket1 = int(input('Enter your ticket amount:'))
if(age1 < 12):
	discount1 = ticket1 * 0.30
elif(age1 > 59):
	discount1 = ticket1 * 0.50
else:
	discount1 = 0
final1 = ticket1 - discount1
total_amount = total_amount + final1

age2 = int(input('Enter age of person 2:'))
ticket2 = int(input('Enter your ticket amount:'))
if(age2 < 12):
	discount = ticket1 * 0.30
elif(age2 > 59):
	discount2 = ticket1 * 0.50
else:
	discount2 = 0
final2 = ticket2 - discount2
total_amount = total_amount + final2

age3 = int(input('Enter age of person 3:'))
ticket3 = int(input('Enter your ticket amount:'))
if(age3 < 12):
	discount3 = ticket1 * 0.30
elif(age3 < 59):
	discount3 = ticket1 * 0.50
else:
	discount3 = 0
final3 = ticket3 - discount3
total_amount = total_amount + final3

age4 = int(input('Enter age of person 4:'))
ticket4 = int(input('Enter your ticket amount:'))
if(age4 < 12):
	discount4 = ticket1 * 0.30
elif(age4 < 59):
	discount4 = ticket1 * 0.50
else:
	discount4 = 0
final4 = ticket4 - discount4
total_amount = total_amount + final4

age5 = int(input('Enter age of person 5:'))
ticket5 = int(input('Enter your ticket amount:'))
if(age5 < 12):
	discount5 = ticket1 * 0.30
elif(age5 < 59):
	discount5 = ticket1 * 0.50
else:
	discount5 = 0
final5 = ticket5 - discount5
total_amount = total_amount + final5
print('Total amount for 5 persons:',total_amount)