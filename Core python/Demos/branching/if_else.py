# 2. if - else
# where we decide which block of code will execute.
# if the condition is true then if block of code will execute.
# if the condition is false then else block of code will execute.

# syntax:
# if(condition):
   # block of code
# else:
   # block of code 

num = int(input("Enter number:"))
if(num > 0):
    print(f'{num} is a positive number')
else:
    print(f'{num} is a negative number')