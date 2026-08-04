# Write a program to prompt user to enter userid and password.after verifying userid and password display a 4 digit random number and ask user to enter the same number then show him success
# message otherwise failed (something like captcha)

import random
correct_userid = 'snehal'
correct_password =2004
user_id = input('Enter user id:')
password = int(input('Enter password:'))
if(user_id == correct_userid and password == correct_password):
	print('login successful')
	capt = random.randint( 1000,9999 )
	print('verification code:',capt)
	user_input = int(input('Enter the verification code:'))
	if(user_input == capt):
		print('verification successful')
	else:
		print('verification failed')
else:
	print('Invalid user id or password')