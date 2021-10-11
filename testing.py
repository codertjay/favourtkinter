from tkinter import *
tjay = Tk()
"""
lab = Label(tjay,text="favour",fg="red",bg="blue")

lab.grid()
tjay.mainloop()
"""

def clickme():
    mylab = Label(tjay,text="working",bg="yellow",borderwidth=20)
    mylab.pack()

myb = Button(tjay,text="click me",fg="blue",bg="red",padx=20,pady=10,command=clickme)
myb.pack()
tjay.mainloop()





