from tkinter import *

window = Tk()

def click():
    global count
    count += 1
    print(count)

photo = PhotoImage(file='like.png')

button = Button(window,
                text='click here',
                command=click,
                font=('comic sans',30),
                fg='#000000',
                bg='grey',
                activeforeground='#000000',
                activebackground='grey',
                state=ACTIVE,
                image=photo,
                compound='top')
button.pack()

window.mainloop()
