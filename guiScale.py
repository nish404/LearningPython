from tkinter import *

window = Tk()

def submit():
    print("the temperature is "+str(scale.get())+" degrees F")

scale = Scale(window,
                from_=0,
                to=100,
                length=600,
                orient=VERTICAL, #orientation of scale
                font=('arial',20),
                tickinterval=10, #adds numeric indicator for value
                showvalue=0, #hide current value
                resolution=5, #increment of slider
                troughcolor='blue',
                fg='red',
                bg='black'
                )

scale.set((scale['from']-scale['to']/2)+scale['to']) #set current value of slider
#scale.set(50) #set the current value of the slider     
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()
