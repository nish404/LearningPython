from tkinter import *

window = Tk()

def display():
    if(x.get()==1):
        print("you agree")
    else:
        print("you don't agree")
x = IntVar()

img = PhotoImage(file='pythonlogo.png')

check_button = Checkbutton(window,
                            text="I agree to something",
                            variable=x,
                            onvalue=1,
                            offvalue=0,
                            command=display,
                            font=('Arial',20),
                            fg='red',
                            bg='black',
                            activeforeground='red',
                            activebackground='black',
                            padx=25,
                            pady=10,
                            image=img,
                            compound=LEFT)
check_button.pack()
window.mainloop()
