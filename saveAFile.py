from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Nish\\Python",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("All files",".*")])
    if file is None: #eliminates the exception error
        return
    filetext = str(text.get(1.0,END))
    #filetext = input("enter some text: ") //use if you want to use the console to enter some text
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='save',command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()