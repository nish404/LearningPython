from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("you ordered pizza")
    elif(x.get()==1):
        print("you ordered a hamburger")
    elif(x.get()==2):
        print("you ordered a hotdog")
    else:
        print("huh")

window = Tk()

pizza = PhotoImage(file='pizza.png')
hamburger = PhotoImage(file='hamburger.png')
hotdog = PhotoImage(file='hotdog.png')
foodimages = [pizza,hamburger,hotdog]

x = IntVar()

for i in range(len(food)):
    radioButton = Radiobutton(window,
                                text=food[i], #adds text to radio buttons
                                variable=x, #groups radiobuttons together if they share the same variable
                                value=i, #assigns each radiobutton a different value
                                padx=25, #adds padding on x axis
                                font=('impact',50),
                                image=foodimages[i], #adds images to radiobutton
                                compound='left', #adds image and text
                                indicatoron=0, #eliminate circle indicators
                                width= 1000, #sets width of radiobuttons
                                command=order #set commanad of radiobutton to function
                                )
    radioButton.pack(anchor=W)

window.mainloop()
