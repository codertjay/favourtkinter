from tkinter import *
tjay =Tk()

e=Entry(tjay,width=35,bd=10)
e.grid(row=0,column=0,columnspan=3)

def clickme(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    f_number = e.get()
    global f_num
    global math
    math ="addition"
    f_num= int(f_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0,f_num + int(second_number))
    elif math == "minus":
        e.insert(0, f_num - int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))
    elif math == "multiply":
        e.insert(0, f_num * int(second_number))


def button_clr():
    e.delete(0, END)


def button_multiply():
    f_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(f_number)
    e.delete(0, END)

def button_minus():
    f_number = e.get()
    global f_num
    global math
    math = "minus"
    f_num = int(f_number)
    e.delete(0, END)

def button_division():
    f_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(f_number)
    e.delete(0, END)


button_1=Button(tjay,text=1,padx=20,pady=20,command=lambda :clickme(1))
button_2=Button(tjay,text=2,padx=20,pady=20,command=lambda :clickme(2))
button_3=Button(tjay,text=3,padx=20,pady=20,command=lambda :clickme(3))
button_4=Button(tjay,text=4,padx=20,pady=20,command=lambda :clickme(4))
button_5=Button(tjay,text=5,padx=20,pady=20,command=lambda :clickme(5))
button_6=Button(tjay,text=6,padx=20,pady=20,command=lambda :clickme(6))
button_7=Button(tjay,text=7,padx=20,pady=20,command=lambda :clickme(7))
button_8=Button(tjay,text=8,padx=20,pady=20,command=lambda :clickme(8))
button_9=Button(tjay,text=9,padx=20,pady=20,command=lambda :clickme(9))
button_0=Button(tjay,text=0,padx=20,pady=20,command=lambda :clickme(0))
button_add=Button(tjay,text="+",padx=40,pady=20,command=button_add)

button_clear=Button(tjay,text="clr",padx=30,pady=20,command=button_clr)
button_equal=Button(tjay,text="=",padx=30,pady=20,command=button_equal)
button_multiply=Button(tjay,text="x",padx=30,pady=20,command=button_multiply)
button_minus=Button(tjay,text="-",padx=30,pady=20,command=button_minus)
button_divide=Button(tjay,text="/",padx=30,pady=20,command=button_division)

button_1.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=0)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_minus.grid(row=5,column=0)
button_clear.grid(row=5,column=1)
button_equal.grid(row=5,column=2)
button_multiply.grid(row=6,column=0)
button_minus.grid(row=6,column=1)
button_divide.grid(row=6,column=2)


tjay.mainloop()



