from tkinter import *
from tkinter import messagebox #import messagebox library

window = Tk()

def click():
    #messagebox.showinfo(title="this is an info message",message='you are a person')
    #while(True):
    #    messagebox.showwarning(title="WARNING!",message='YOU HAVE A VIRUS')
    #messagebox.showerror(title="ERROR",message='404 link not found')
    #if messagebox.askokcancel(title="ask ok cancel",message='do you want to do the thing'):
        #print('you did a thing')
    #else:
        #print('you canceled a thing')
    #messagebox.askretrycancel(title='ask retry cancel',message='do you want to retry a thing')
    #messagebox.askyesno(title='ask yes no',message='do you like cake ')
    #answer = messagebox.askquestion(title='ask question',message='is the sky blue? ')
    #if answer == ('yes'):
    #    print('you passed the test')
    #else:
    #    print('you may need to see an eye doctor')
    answer = messagebox.askyesnocancel(title='yes no cancel',message='do you like to code?',icon='warning')
    if (answer==True):
        print('you like to code')
    elif(answer==False):
        print("then why are you watching a video on coding ")
    else:
        print('you have dodged the question')

button = Button(window,command=click,text='click here')
button.pack()

window.mainloop()
