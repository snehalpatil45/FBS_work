from datastore import Datastore

class Admin:
    def __init__(self):
        self.ds = Datastore()
        ch = 0
        while(ch != 6):
            print('''Please select option
                  1. Add emp
                  2. upd emp
                  3. del emp
                  4. search emp
                  5. show all emp
                  6.logout
                  ''')
            ch = input('Enter choice:')
            if(ch == '1'):
                self.addEmp()
            elif(ch == '5'):
                pass
            elif(ch == '6'):
                print('Logged out...')
            else:
                print('Invalid choice...')

    def addEmp(self):
        id = input('Enter ID:')
        name = input('Enter Name:')
        sal = float(input('Enter salary:'))
        dept = input('Enter Department:')

    def showAllEmp(self):
        pass

if(__name__ == '__main__'):
    Admin()
                