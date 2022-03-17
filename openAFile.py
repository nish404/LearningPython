from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\Users\\nish\Python", 
                                            title="open file ok?,",
                                            typenames=(("text files","*.txt","all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

    #for mac you would not include filetypes as it does not exist as an option

window = Tk()

button = Button(window,text='open',command=openFile)
button.pack()

window.mainloop()