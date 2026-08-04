# write a program to check if person is eligible for marry or not.

gender = input('Enter gender(M/F):')
age = int(input('Enter age:'))
if( gender.lower() in ['f','female']):
	if(age >= 18):
		print('Eligible for marriage')
	else:
		print('Pehle padhai kar le')
else:
	if(age >= 21):
		print('Eligible for marriage')
	else:
		print('Pehle bade ho jao')