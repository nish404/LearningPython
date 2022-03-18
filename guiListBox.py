# listbox = a listing of selectable text items within it's own container 

from tkinter import *
from typing import List

window = Tk()

def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    
    print("you have ordered: ")
    for i in food:
        print(i)
    #print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

listbox = Listbox(window,
                    bg="#f7ffde",
                    font=('Constantia',35),
                    width=12,
                    selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry()
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()

window.mainloop()
