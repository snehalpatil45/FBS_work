from tkinter import *

window = Tk()
window.geometry('300x400')
window.title('First program')
window.config(bg='#0f172a')

txt = Label(
    window,
    text = 'Snehal',
    font = ('Verdana', 20, 'bold'),
    bg = '#0284c7',
    fg = 'cyan',
    pady = 20)

txt.pack()
window.mainloop()