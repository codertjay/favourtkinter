from tkinter import *
tjay = Tk()

#creting a button to work so i have to define a label and function
def myclick():
    mylabel = Label(tjay,text="button is working")
    mylabel.pack()

mybutton1 = Button(tjay,text="click me!",state=DISABLED)#I JUST DISABLED THE BUTTON
mybutton2 = Button(tjay,text="click me!",padx=200 )#this is a straight column
mybutton3 = Button(tjay,text="click me!",pady=200 )#this is a straight row

#here i wants to call the function
#so i would say mybutton.command=myclick
#see it in label four
mybutton4= Button(tjay,text="click me!",command = myclick)
mybutton5=Button(tjay,text="click me!",bg="black",fg="red")#i changed the back grond and fore ground color

mybutton1.pack()
mybutton2.pack()
mybutton3.pack()
mybutton4.pack()
mybutton5.pack()

tjay.mainloop()





