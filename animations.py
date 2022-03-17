from tkinter import *
import time

# constants = variables that do not change throughout the program
#             common naming convention is all 'UPPERCASE'
WIDTH = 900 
HEIGHT = 900
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

backgroundImage = PhotoImage(file='outerspace.gif')
background = canvas.create_image(0,0,image=backgroundImage,anchor=NW)

image = PhotoImage(file='alien.png')
alien = canvas.create_image(0,0,image=image,anchor=NW)

imageWidth = image.width()
imageHeight = image.height()

while True:
    coordinates = canvas.coords(alien)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-imageWidth) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-imageHeight) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(alien,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()