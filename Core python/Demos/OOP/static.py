# static variable
#1. class level variable
#2.use class name or object name to access
#3.single copy will created and shared to all objects

# non - static variable
#1. object/instance level variable
#2. use object name to access
#3.copies created according to the no.of objects.

class BankAccount:
    branch = 'SBI,FC Road'
    def __init__(self,ac_no,bal,holder_name):
        self.ac_no = ac_no
        self.bal = bal
        self.holder_nm = holder_name
    
    def display(self):
        data = f'ACC NO:{self.ac_no}\nBALANCE:{self.bal}\nHOLDER NAME:{self.holder_nm}\nBranch:{BankAccount.branch}'
        return data
    
b1 = BankAccount(10001,151,'pandurang')
b2 = BankAccount(10002,200,'Tushar')
print(b1.ac_no)
# del b1
res = b1.display()
print(res)
print('##################')
res = b2.display()
print(res)
print('##################')
print(BankAccount.branch)
print(b1.branch)