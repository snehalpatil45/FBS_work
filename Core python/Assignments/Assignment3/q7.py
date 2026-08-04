# wap to check if user has entered correct userid and password.

correct_userid = 'snehal'
correct_password = 2004
user_id = input('Enter userid :')
password = int(input('Enter password:'))
if( user_id == correct_userid  and password == correct_password ):
	print('Login successful')
else:
	print('Invalid Id and password')