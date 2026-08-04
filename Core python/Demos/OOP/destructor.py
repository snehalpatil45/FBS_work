class BankAccount:
    def __init__(self,ac_no,bal,holder_name):
        self.ac_no = ac_no
        self.bal = bal
        self.holder_nm = holder_name
    
    def display(self):
        data = f'ACC NO:{self.ac_no}\nBALANCE:{self.bal}\nHOLDER NAME:{self.holder_nm}'
        return data
    
    def __del__(self):
        print('This is destructor...')

b1 = BankAccount(10001,151,'pandurang')
# del b1
res = b1.display()
print(res)