from tkinter import *
from tkinter import messagebox

def addition():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    sum = num1 + num2
    messagebox.showinfo(message=f'Addition:{sum}')

window = Tk()
window.geometry('300x400')
window.title('Addition program')
window.config(bg='#0f172a')

heading = Label(
    window,
    text = 'Addition',
    font = ('Verdana', 20, 'bold'),
    bg = '#0284c7',
    fg = 'cyan',
    pady = 20)

heading.pack()
frame =Frame(window,pady = 10)

num1_txt = Label(
    frame,
    text = 'Enter number 1:',
    font =('Arial',12),
    bg ='#1e1e2f',
    fg = 'white'
)
num1_txt.grid(row = 0,column = 0)

num2_txt = Label(
    frame,
    text = 'Enter number 2:',
    font =('Arial',12),
    bg ='#1e1e2f',
    fg = 'white'
)
num2_txt.grid(row = 1,column = 0)

num1_entry = Entry(
    frame,
    font =('Arial',12),
    bg ='#1e1e2f',
    fg = 'white')
num1_entry.grid(row =0,column =1)

num2_entry = Entry(
    frame, 
    font =('Arial',12),
    bg ='#1e1e2f',
    fg = 'white')
num2_entry.grid(row =1,column =1)

btn = Button(
    frame,text ='ADD',command=addition
)
btn.grid(row =2,column=0,columnspan=2)

frame.pack()

window.mainloop()