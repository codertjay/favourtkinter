from tkinter import *
from PIL import ImageTk,Image

tjay = Tk()

frame = LabelFrame(tjay,text="this is my frame...",padx=100,pady = 10)
frame.pack(padx=10,pady=10)

but1 = Button(tjay,text='click me',padx=20,pady=15,bg="blue")
but1.pack()


tjay.mainloop()

