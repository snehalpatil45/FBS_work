# input 5 subject marks from user and display grade.(e.g first class , second class)

physics = int(input('Enter the marks of physics:'))
chemistry = int(input('Enter the marks of chemistry:'))
math = int(input('Enter the marks of math:'))
biology = int(input('Enter the marks of biology:'))
geography = int(input('Enter the marks of geography:'))
total = physics + chemistry + math + biology + geography
percentage = total / 5
if(percentage >= 76 and percentage <= 100):
	print('Grade:A')
elif(percentage >= 61 and percentage <= 75):
	print('Grade:B')
elif(percentage >= 51 and percentage <= 60):
	print('Grade:C')
elif(percentage >= 41 and percentage <= 50):
	print('Grade:D')
elif(percentage >= 0 and percentage <= 40):
	print('Fail,better luck next time')
else:
	print('Invalid percentage')	