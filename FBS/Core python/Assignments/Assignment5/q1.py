# write a program to prompt user to enter userid and password .if id and password is incorrect give him chance to reenter the credentials.
# let him try 3 times.after that program to terminate.


user_id = 'snehal'
password = '2004'
count = 0
while (count < 3):
    uid = input('Enter user id :')
    pwd = input('Enter password:')

    if (uid == user_id and pwd == password):
        print('login Successful')
        break
    else:
        print('Wrong credentials')
        count = count + 1
if(count == 3):
    print('program terminated')