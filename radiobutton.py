from tkinter import *

tjay = Tk()
tjay.title("code with codertj")

r =  IntVar()
r.set('2')

mide = [
    ("rice","rice"),
    ("beans","beans"),
    ("pepper","pepper"),
    ("chicken","chicken"),
]

pizza =


def clicked(value):
    mylabel2= Label(tjay,text = value).pack()

Radiobutton(tjay,text="Option 1",variable=r,value=1,command=lambda :clicked(r.get())).pack()
Radiobutton(tjay,text="Option 2",variable=r,value=2,command=lambda :clicked(r.get())).pack()

mylabel = Label(tjay,text=r.get()).pack()

tjay.mainloop()