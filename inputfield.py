from tkinter import *

tjay=Tk()
"""
#Entry is use to  word in tkinter
ent=Entry(tjay,width=30,bg = "blue",fg="white",borderwidth=5)
ent.pack()

#borderwidth:this means there would be a border in the label or entry or button
#width: this means that the entry width would be 30 in what i did
"""

#now let us do something let us make a user input a word in the entry and use it
#here i use a function in the entry by using ent.get so that way any thing
#the user type once i click the button it print it out

#this is the entry field
ent=Entry(tjay,width=30,bg = "blue",fg="white",borderwidth=5)
#this shows in the entry box i.e enter your name
ent.insert(0,"enter your name:")
ent.pack()

#this is the function but i use ent.get in the label
def myclick():
#i use ent.get to get what is in the entry box and place it on the function
    myl=Label(tjay,text="hello "+ent.get())
    myl.pack()
#this is the botton
myb = Button(tjay,text="click",command=myclick)
myb.pack()




tjay.mainloop()

