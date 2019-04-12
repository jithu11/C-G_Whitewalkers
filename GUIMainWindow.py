import tkinter
from tkinter import messagebox, Entry, Label

m = tkinter.Tk()
m.title("Bank Application ")

Label(m, text='First Name').grid(row=0)
Label(m, text='Last Name').grid(row=1)
e1 = Entry(m)
e2 = Entry(m)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


def hello():
    name = e1.get()
    init = e2.get()
    messagebox.showinfo("Alert", "Hello Mr." + name + " " + init)


button = tkinter.Button(m, text='say hello', width=25, command=hello)
button.grid(row=5, column=1)

m.mainloop()