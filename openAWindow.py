from tkinter import *

def create_window():
    new_window = Tk()        #Tk() = a new independent window, useful for login screen
    #new_window = Toplevel() #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    
    old_window.destroy()     #close out the old window

old_window = Tk()            #this would be the 'bottom' level window

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()