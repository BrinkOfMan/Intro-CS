#Day 30

import time
import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import ttk

#=====Layout models=====

#place (exact x,y coords)
##for every widget

#pack (fits widgets to the container in the order added)
##only really care about the order that they go in, not necessarily the location
##great for testing things

#grid (uses columns and rows)
##The grid gets defined by how many things you put in

#======Other stuff======

#Use the tag <global> when calling a global variable within a local function

win = tk.Tk()                            
my_label = tk.Label(win, text='Square doodad')  
my_label.pack()

color = ''

#Create a canvas
my_canvas = tk.Canvas(win, width=300, height=200)
my_canvas.pack()

def rKey(event):
    global color
    print('Square color will now be red.')
    color = 'red'

def gKey(event):
    global color
    print('Square color will now be green.')
    color = 'green'

def bKey(event):
    global color
    print('Square color will now be blue.')
    color = 'blue'

#Bind key presses to the window
win.bind('<r>', rKey)
win.bind('<g>', gKey)
win.bind('<b>', bKey)

#Draw a rectangle when the user clicks on the canvas
def mouseClick(event):
    global color
    mx = event.x
    my = event.y
    my_canvas.create_rectangle(mx, my, mx+20, my+20, width=5, outline=color)

def mouseDrag(event):
    global color
    mx = event.x
    my = event.y
    time.sleep(0.0050)
    my_canvas.create_rectangle(mx, my, mx+20, my+20, width=5, outline=color)

def info(event):
    print('Left-click on the canvas to draw a single square.')
    print('Right-click and hold to draw multiple squares.')

#Bind the mouse click event to my_canvas
my_canvas.bind('<Button-1>', mouseClick)
my_canvas.bind('<B3-Motion>', mouseDrag)

quit_button = tk.Button(win, text='Quit', command=win.destroy)
quit_button.pack()

win.mainloop()


#======================Bouncy ball thing======================
win = tk.Tk()                            
my_label = tk.Label(win, text='Circle doodad')  
my_label.pack()

CW = 300
CH = 500
canvas = tk.Canvas(win, width = CW, height = CH)
canvas.pack()
circle = canvas.create_oval(0,0,30,30, fill='blue')


dx = 5
dy = 3
def redraw():
    global dx, dy
    c = canvas.coords(circle)
    if c[0] < 0 or c[2] > CW:
        dx = -1*dx
    if c[1] < 0 or c[3] > CH:
        dy = -1*dy
    canvas.move(circle,dx,dy)
    canvas.after(33,redraw)
        
canvas.after(33,redraw)

win.mainloop()
