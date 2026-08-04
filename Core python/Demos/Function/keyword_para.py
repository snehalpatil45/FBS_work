# keyword parameter
#1. to neglect position parameter concept
#2.assigning value to parameter in function call
#3.name of parameters in function call and function def should be same.
#4. flow from right to left.

def emp(id,name,sal,dept):
    print('ID:',id)
    print('Name:',name)
    print('Salary:',sal)
    print('Department:',dept)

emp(101,'abc',7000,'DA')
print('##3')
emp(name='xyz',sal=8000,dept='testing',id=420)