from tkinter import *

def moveUp(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-20)
def moveDown(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+20)
def moveLeft(event):
    label.place(x=label.winfo_x()-20,y=label.winfo_y())
def moveRight(event):
    label.place(x=label.winfo_x()+20,y=label.winfo_y())

window = Tk()

window.geometry("1000x1000")
window.bind("<w>",moveUp)
window.bind("<s>",moveDown)
window.bind("<a>",moveLeft)
window.bind("<d>",moveRight)
window.bind("<Up>",moveUp)
window.bind("<Down>",moveDown)
window.bind("<Left>",moveLeft)
window.bind("<Right>",moveRight)

image = PhotoImage(file='car.png')

label = Label(window,image=image)
label.place(x=0,y=0)

window.mainloop()
