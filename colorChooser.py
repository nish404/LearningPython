from tkinter import *
from tkinter import colorchooser #submodule

window = Tk()
window.geometry("420x420")

def click():
    #color = colorchooser.askcolor()
    #print(color)
    #colorHex = color[1]
    #print(colorHex)
    #window.config(bg=colorHex) #change background color
    window.config(bg=colorchooser.askcolor()[1]) #creates one line of code

button = Button(window,text='click here',command=click)
button.pack()

window.mainloop()
