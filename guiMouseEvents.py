from tkinter import *

def doSomething(event):
    print("mouse coordinates: " + str(event.x) +","+ str(event.y))

window = Tk()
# window.bind(event,function)
#window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll wheel (click on it)
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething) #hold and release mouse
#window.bind("<Enter>",doSomething) #entering the window
#window.bind("<Leave>",doSomething) #leaving the window
window.bind("<Motion>",doSomething) #where the mouse moves

window.mainloop()
