from tkinter import *
tjay =Tk()
tjay.title("simple calculator")


e = Entry(tjay,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#function for clicking number
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

#function for clearing number
def button_clr():
    e.delete(0,END)

#fuction for adding the button
def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

#function for equal
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0,f_num + int(second_number))



#define buttons the buttons look like
button_1=Button(tjay, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2=Button(tjay, text="2", padx=20, pady=10, command=lambda:button_click(2))
button_3=Button(tjay, text="3", padx=20, pady=10, command=lambda:button_click(3))
button_4=Button(tjay, text="4", padx=20, pady=10, command=lambda:button_click(4))
button_5=Button(tjay, text="5", padx=20, pady=10, command=lambda:button_click(5))
button_6=Button(tjay, text="6", padx=20, pady=10, command=lambda:button_click(6))
button_7=Button(tjay, text="7", padx=20, pady=10, command=lambda:button_click(7))
button_8=Button(tjay, text="8", padx=20, pady=10, command=lambda:button_click(8))
button_9=Button(tjay, text="9", padx=20, pady=10, command=lambda:button_click(9))
button_0=Button(tjay, text="0", padx=20, pady=10, command=lambda:button_click(0))
button_add=Button(tjay, text="+", padx=30, pady=10, command=button_add)
button_equal=Button(tjay, text="=", padx=30, pady=10, command=button_equal)
button_clr=Button(tjay, text="clr", padx=25, pady=10, command=button_clr)
button_minus=Button(tjay, text="-", padx=25, pady=10, command=button_minus)
button_multiply=Button(tjay, text="x", padx=25, pady=10, command=button_multiply)
button_divide=Button(tjay, text="/", padx=25, pady=10, command=button_divide)

#put the button onm the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1,columnspan=1)
button_equal.grid(row=5,column=2)
button_clr.grid(row=5,column=0)

button_minus.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_multiply.grid(row=6,column=2)

tjay.mainloop()
