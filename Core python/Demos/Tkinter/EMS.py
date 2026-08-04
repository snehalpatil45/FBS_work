from tkinter import *
from tkinter import messagebox

def clearScreen():
    for widget in window.winfo_children():
        widget.destroy()

def empManage():
    def loadData():
        mylist.delete(0,END)
        with open('FBS/Core python/Demos/Tkinter/emp_details.txt','r') as fp:
            for row in fp:
                mylist.insert(END,row)
    # messagebox.showinfo(message='Login Successful.')
    def addEmp():
        id =id_entry.get()
        nm =nm_entry.get()
        sal = sal_entry.get()
        edata = f'{id},{nm},{sal}'
        mylist.insert(END,edata)
        with open('FBS/Core python/Demos/Tkinter/emp_details.txt','a') as fp:
            fp.write(edata+'\n')
        # messagebox.showinfo(message='Employee added successfully.')

    
    def selEmp():
        edata =mylist.get(ACTIVE)
        elist = edata.split(',')
        id_entry.insert(0, elist[0])
        nm_entry.insert(0, elist[1])
        sal_entry.insert(0, elist[2])

    def updEmp():
        id = id_entry.get()
        nm = nm_entry.get()
        sal = sal_entry.get()
        sal = sal.strip('\n')
        all_emp_list = []
        with open('FBS/Core python/Demos/Tkinter/emp_details.txt','r') as fp:
            for row in fp:
                elist = row.strip().split(',')
                if(elist[0] == id):
                    edata = f'{id},{nm},{sal}'
                    all_emp_list.append(edata)
                else:
                    all_emp_list.append(edata)
        with open('FBS/Core python/Demos/Tkinter/emp_details.txt','w') as fp:
            for edata in all_emp_list:
                fp.write(edata+'\n') 
        loadData()

    def delEmp():
        id_entry.delete(0,END)
        nm_entry.delete(0,END)
        sal_entry.delete(0,END)
    
    clearScreen()

    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)

    id_label = Label(frame1,text='ID:')
    id_entry = Entry(frame1)
    nm_label = Label(frame1,text='Name:')
    nm_entry = Entry(frame1)
    sal_label = Label(frame1,text='Salary:')
    sal_entry = Entry(frame1)

    id_label.grid(row=0,column=0)
    id_entry.grid(row=0,column=1)
    nm_label.grid(row=1,column=0)
    nm_entry.grid(row=1,column=1)
    sal_label.grid(row=2,column=0)
    sal_entry.grid(row=2,column=1)

    frame1.pack()

    add_btn = Button(frame2,text='ADD',command=addEmp)
    sel_btn = Button(frame2,text='SELECT',command=selEmp)
    upd_btn = Button(frame2,text='UPDATE',command=updEmp)
    del_btn = Button(frame2,text='DELETE',command=delEmp)

    add_btn.pack(side=LEFT)
    sel_btn.pack(side=LEFT)
    upd_btn.pack(side=LEFT)
    del_btn.pack(side=LEFT)
    frame2.pack()

    scrollbar=Scrollbar(frame3)
    scrollbar.pack(side=RIGHT,fill=Y)
    mylist = Listbox(frame3,yscrollcommand=scrollbar.set,height=15,width=40)
    mylist.pack(side=LEFT,fill=BOTH)
    scrollbar.config(command=mylist.yview)
    frame3.pack()

    loadData()

def login():
    uid =uid_entry.get()
    passw =passw_entry.get()
    uname ='admin'
    password = '1234'
    if(uid == uname and passw == password):
        empManage()
    else:
        messagebox.showwarning(message='Invalid credentials')

def main():
    uid_label = Label(window,text='User ID:')
    global uid_entry
    uid_entry = Entry(window)

    passw_label = Label(window,text ='password:')
    global passw_entry
    passw_entry = Entry(window)

    btn = Button(window,text ='LOGIN',command =login)

    uid_label.pack()
    uid_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    btn.pack()

if(__name__ == '__main__'):
    window =Tk()
    window.geometry('300x400')

    # main()
    empManage()

    window.mainloop()