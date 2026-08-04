def addEmp(id,name,sal,dept):
    if(id not in emp_detail):
        emp_detail[id] = [id,name,sal,dept]
        return 'Employee added'
    else:
        return f'{id} already available'

def updEmp(id):
    if(id in emp_detail):
        emp = emp_detail[id]
        print("Note:If don't want to change the field leave blank" )
        name = input(f'Enter new name({emp[1]}):') or emp[1]
        sal = input(f'Enter new sal({emp[2]}):') or emp[2]
        dept = input(f'Enter new dept({emp[3]}):') or emp[3]
        emp_detail[id] = [id,name,sal,dept]
        return 'Employee updated succesfully'
    else:
        return f'{id} not exists.'
    
emp_detail = {}
ch = 0
while(ch != '6'):
    print('''please select option:
    1.Add emp
    2.show all emp
    3.update emp
    4.Delete emp
    5.Search emp
    6.Exit
    ''')
    ch = input('Enter choice:')
    if(ch == '1'):
        id = input('Enter ID:')
        name = input('Enter name:')
        sal = float(input('Enter salary:'))
        dept = input('Enter Department:')
        res = addEmp(id,name,sal,dept)
        print(res)
    elif(ch == '2'):
        print(emp_detail)
    elif(ch == '3'):
        id = input('Enter ID:')
        res = updEmp(id)
        print(res)
    elif(ch == '4'):
        id = input('Enter ID to delete:')
        if (id in emp_detail):
            del emp_detail[id]
            print('Employee deleted successfully')
        else:
            print('Employee not found')
    elif(ch == '5'):
        id = input('Enter ID to search:')
        if id in emp_detail:
            emp = emp_detail[id]
            print("\nEmployee Found:")
            print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}, Dept: {emp[3]}")
        else:
            print("Employee not found")
    elif(ch == '6'):
        print('Mandal aabhari aahe!!!!!')
    else:
        print('Invalid choice....')