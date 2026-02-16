#take input
num1 = input('Enter number:')
#print(num1)
#print(type(num1))   - < class 'str' >
num1 = int(input('Enter number:'))   
#print(type(num1))   - < class int >
#Typecasting : convert data into one type to another type.

### addition:
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
#perform operation
sum = num1 + num2

#display result
#print(sum)
#print("Addition is:",sum)   - print function takes multiple parameter.
#print("Addition of" +str(num1)+ '&'+str(num2)+ 'is'+str(sum)+'.')
print(f'Addition of {num1}  & {num2}  is {sum}')   #f-string - formatted string, 
#it is way to put variables or expressions directly inside a string.
