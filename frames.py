# frames = a rectangular container to group and hold widgets 
from tkinter import *
from tkinter import font

window = Tk()

frame = Frame(window,bg='red',bd=5,relief=SUNKEN)
frame.place(x=0,y=0)
#frame.pack(side=BOTTOM)

Button(frame,text="W",font=('verdana',25),width=3).pack(side=TOP) #won't be able to modify button by name anymore
Button(frame,text="A",font=('verdana',25),width=3).pack(side=LEFT)
Button(frame,text="S",font=('verdana',25),width=3).pack(side=LEFT)
Button(frame,text="D",font=('verdana',25),width=3).pack(side=LEFT)

window.mainloop()