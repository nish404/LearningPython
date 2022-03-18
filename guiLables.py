from tkinter import *
# label = an area widget that holds text and/or an image within a window 

window = Tk()

img = PhotoImage(file='msft logo.png')

label = Label(window,
            text="program1",
            font=('monospace',40,'bold'),
            fg='grey',
            bg='light grey',
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=img,
            compound='bottom')
label.pack()
#label.place(x=0,y=0)

window.mainloop()
