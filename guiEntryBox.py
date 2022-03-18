# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    text = entry.get()
    print(text)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
                font=('arial',50),
                fg="#4f4f4f",
                bg="black")

#entry.insert(0,'User1')
#entry.config(show="*")
#entry.config(state=DISABLED)

entry.pack(side=LEFT)

submitButton = Button(window,text="submit",command=submit)
submitButton.pack(side=RIGHT)

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack(side=RIGHT)

backspaceButton = Button(window,text="backspace",command=backspace)
backspaceButton.pack(side=RIGHT)

window.mainloop()
