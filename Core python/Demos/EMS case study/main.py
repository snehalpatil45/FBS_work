def main():
    ch = 0
    while(ch != 2):
        print('''Please select option:
              1.Login
              2.Exit''')
        ch = input('Enter choice:')
        if(ch == '1'):
            login()
        elif(ch == '2'):
            print('Thank you for choosing us!')
        else:
            print('Invalid choice...')

def login():
    print('##########LOGIN PAGE###########')
    uname = 'admin'
    passw = '1234'
    username = input('Enter username:')
    password = input('Enter password:')
    if(uname == username and passw == password):
        print('Logged in Successful.....')
    else:
        print('Invalid credentials...')

if(__name__ == '__main__'):
    main()