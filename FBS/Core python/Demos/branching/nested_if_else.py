# 3. Nested if else:
# if next condition is depends on previous condition according to situation then we use nested if else.
# for multiple conditions we use nested if else.

gender = input('Enter gender(M/F):')
age = int(input('Enter age:'))
if(gender.lower() in ['f','female']):
    if(age >= 18):
       print('Eligible for marriage.')
    else:
       print('pahle padhai kar le.')
else:
   if(age >= 21):
      print('Eligible for marriage.')
   else:
      print('Pehle bade ho jao.')