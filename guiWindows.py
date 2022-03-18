from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets 

window = Tk() # instantiate an instance of a window 
window.geometry("400x400") 
window.title("First GUI window")

icon = PhotoImage(file='msft logo.png')
window.iconphoto(True,icon)
window.config(background='#191a19')

window.mainloop() # place window on a computer screen, listen for events
