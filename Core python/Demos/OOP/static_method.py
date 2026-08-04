# static method:
#1.class level method
#2. no need to mention self in method defination
#3.use class name to access these method
#4.for accessing static method using object,mention @staticmethod decorator

class BankAccount:
    branch = 'SBI,FC Road'
    def __init__(self,ac_no,bal,holder_name):
        self.ac_no = ac_no
        self.bal = bal
        self.holder_nm = holder_name
    
    def display(self):
        data = f'ACC NO:{self.ac_no}\nBALANCE:{self.bal}\nHOLDER NAME:{self.holder_nm}\nBranch:{BankAccount.branch}'
        return data
    
    @staticmethod # decorator
    def displayBranch():
        return BankAccount.branch
    
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
#print(BankAccount.branch)
print(BankAccount.displayBranch())
# b1.displayBranch() - error
print(b1.displayBranch()) # use decorator to access it