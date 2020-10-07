#Ethan Brinkman
#Homework 21: 1, 2, 3

import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import ttk
import random as rand

#===============Problems 1 and 2===============

window = tk.Tk()                            #Creates an application window
my_label = tk.Label(window, text='Flag Creator')  #Create a window label
my_label.pack()

my_canvas = tk.Canvas(window, width=400, height=300)
my_canvas.pack()

def France():                                                       #Function for creating the flag of France
    my_canvas.create_rectangle(50,50,150,250,fill='blue')           #Blue section
    my_canvas.create_rectangle(150,50,250,250,fill='white')         #White section
    my_canvas.create_rectangle(250,50,350,250,fill='red')           #Red section
    my_canvas.create_rectangle(50,50,350,250,width=3)               #A e s t h e t i c outline

def Germany():
    my_canvas.create_rectangle(50,50,350,116,fill='black')          #Black section
    my_canvas.create_rectangle(50,116,350,183,fill='red')           #Red section
    my_canvas.create_rectangle(50,183,350,250,fill='yellow')        #Yellow section  
    my_canvas.create_rectangle(50,50,350,250,width=3)               #Another a e s t h e t i c outline

def Japan():
    my_canvas.create_rectangle(50,50,350,250,fill='white',width=3)  #White background (with a e s t h e t i c outline)
    my_canvas.create_oval(150,100,250,200,fill='red', outline='red')

draw_button = tk.Button(window, text='France', command=France)
draw_button.pack()

draw_button = tk.Button(window, text='Germany', command=Germany)
draw_button.pack()

draw_button = tk.Button(window, text='Japan', command=Japan)
draw_button.pack()

quit_button = tk.Button(window, text='Quit', command=window.destroy)
quit_button.pack()

window.mainloop()

print('Please hit the "Quit" button when you are finished creating flags.')

#===================Problem 3===================

window = tk.Tk()                            
my_label = tk.Label(window, text='Circle Creator')  
my_label.pack()

my_canvas = tk.Canvas(window, width=400, height=300)
my_canvas.pack()

def randCircle():
    X1 = rand.randrange(10,341)         #X1 random coordinate
    X2 = X1 + rand.randrange(20,51)     #X2 coordinate is between 20 and 50 pixels larger than X1
    Y1 = rand.randrange(10,241)         #Y1 random coordinate
    Y2 = Y1 + (X2 - X1)                 #Making the distance between Y1 <--> Y2 the same as the distance between X1 <--> X2

    r = rand.randrange(255)             #Create the random colors
    g = rand.randrange(255)
    b = rand.randrange(255)
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    print (color)
    
    my_canvas.create_oval(X1, Y1, X2, Y2, fill=color, outline='black')


draw_button = tk.Button(window, text='Draw a circle', command=randCircle)
draw_button.pack()

quit_button = tk.Button(window, text='Quit', command=window.destroy)
quit_button.pack()

window.mainloop()
