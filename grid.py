# grid() = geometry manager that organizes widgets in a table-like structure in a parent widget
from tkinter import *

def submit():
    pass

window = Tk()

titleLabel = Label(window,text="Enter your info: ",font=("Didot",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First Name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last Name: ",bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailAddressLabel = Label(window,text="Email Address: ",width=30,bg="blue").grid(row=3,column=0)
emailAddressEntry = Entry(window).grid(row=3,column=1)

Button(window,text="Submit",command=submit).grid(row=4,column=0,columnspan=2) #columnspan = takes up more than one column and places them in between columns

window.mainloop()