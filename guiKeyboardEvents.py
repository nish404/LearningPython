from tkinter import *

def doSomething(event):
    print("you did a thing")

def anyKey(event):
    #print("you pressed " + event.keysym)
    label.config(text=event.keysym)

window = Tk()


# window.bind(event,function)
window.bind("<Return>",doSomething)
window.bind("q",quit)
window.bind("<Key>",anyKey)

label = Label(window,font=("futura",100))
label.pack()

window.mainloop()
