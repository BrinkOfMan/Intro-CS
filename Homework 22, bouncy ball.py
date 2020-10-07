#Ethan Brinkman
#Homework 22: 1, 2, 3
#Due 4/29/2019

import time
import random as rand
import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import ttk

#===============Number 1===============

win = tk.Tk()
win.title('Ball Bouncing Thing')

CW = 500
CH = 500
canvas = tk.Canvas(win, width = CW, height = CH)
canvas.pack()
circle = canvas.create_oval(0,0,30,30, fill='orange')

dx = 5
dy = 3
def redraw():
    global dx, dy, circle
    c = canvas.coords(circle)
    if c[0] < 0 or c[2] > CW:
        dx = -1*dx
    if c[1] < 0 or c[3] > CH:
        dy = -1*dy
    canvas.move(circle,dx,dy)
    canvas.after(33,redraw)
        
canvas.after(33,redraw)

def colorChange(event):
    global circle
    r = rand.randrange(255)     #Create the random colors
    g = rand.randrange(255)
    b = rand.randrange(255)
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    canvas.itemconfig(circle, fill=color)
    #Using itemconfig to change the state of circle

def sizeChange(event):
    global circle
    x0, y0, x1, y1 = canvas.coords(circle)
    randChange = rand.randrange(-5,8)
    #Use this to create a random size change in the circle (between -5 and 7)
    print('Size change of:',randChange)
    
    if x1+randChange > CW or y1+randChange > CW:
        #Don't change size if the new size is outside of the frame
        pass
    else:
        canvas.coords(circle, x0, y0, x1 + randChange, y1 + randChange)
        #Change the size
    

print('#'*59+'\n\nPress "c" to change the color.\n\nPress "s" to change the size.\n\n'+'#'*59)
win.bind('<c>', colorChange)
win.bind('<s>', sizeChange)

quitButton = tk.Button(win, text='Next program', command=win.destroy)
quitButton.pack()

win.mainloop()

#===============Number 2===============

win = tk.Tk()
win.title('Smiley Face Thing')
CW = 700
CH = 700
canvas = tk.Canvas(win, width = CW, height = CH)
canvas.pack()

def createface(event):
    mx = event.x
    my = event.y
    canvas.create_oval(mx-100, my-100, mx+100, my+100, width=3, fill='yellow')
    canvas.create_oval(mx-50, my-50, mx-30, my-30, width=3, fill='black')
    canvas.create_oval(mx+30, my-50, mx+50, my-30, width=3, fill='black')
    canvas.create_arc(mx-60,my-30,mx+60,my+70, style='pieslice', fill='white', start=180, extent=180, width=3)

print('#'*59+'\n\nLeft-click anywhere on the canvas to create a smiley face.\n\nRight-click and drag to create an abomination.\n\n'+'#'*59)
canvas.bind('<Button-1>', createface)       #Single left-click event
canvas.bind('<Button3-Motion>', createface) #Continuous right-click event

quitButton = tk.Button(win, text='Next program', command=win.destroy)
quitButton.pack()

win.mainloop()

#===============Number 3===============

win = tk.Tk()
win.title('Archery Thing')
CW = 550
CH = 550
canvas = tk.Canvas(win, width = CW, height = CH)
canvas.pack()

nothing = canvas.create_rectangle(0, 0, 550, 550, fill = '#d66508', outline='#d66508')
#This is to prevent clicking outside of the widest circle, but being within the border box
#(Doing this before I added the nothing rectangle would grant the player a point)
white = canvas.create_oval(50, 50, 500, 500, fill='white', tags='1')
black = canvas.create_oval(100, 100, 450, 450, fill='black', tags='3')
blue = canvas.create_oval(150, 150, 400, 400, fill='blue', tags='5')
red = canvas.create_oval(200, 200, 350, 350, fill='red', tags='7')
yellow = canvas.create_oval(250, 250, 300, 300, fill='yellow', tags='9')


def shotTaken(event):
    global Scores, Total
    item = canvas.find_closest(event.x, event.y)
    #This will find the closest item to the click event
    #NOTE: Clicking on a "shot" will find that shot, not the score area
    ##This means if you try to "split an arrow", you will get 0 points
    
    mx = event.x
    my = event.y
    canvas.create_oval(mx-5,my-5,mx+5,my+5, fill='green')
    #Create the shot marker

    #The next part will search through tags and give points accordingly
    if '1' in canvas.gettags(item):
        Scores = Scores[0:]+' 1'
        shotScores.configure(text = Scores)
        #This updates the label by adding the score to the end of the shot scores
        Total[1]+= 1
        totalScore.configure(text = Total)
        #This updates the label by adding the score to the total of all shot scores
        

    elif '3' in canvas.gettags(item):
        Scores = Scores[0:]+' 3'
        shotScores.configure(text = Scores)
        Total[1]+= 3
        totalScore.configure(text = Total)

    elif '5' in canvas.gettags(item):
        Scores = Scores[0:]+' 5'
        shotScores.configure(text = Scores)
        Total[1]+= 5
        totalScore.configure(text = Total)

    elif '7' in canvas.gettags(item):
        Scores = Scores[0:]+' 7'
        shotScores.configure(text = Scores)
        Total[1]+= 7
        totalScore.configure(text = Total)

    elif '9' in canvas.gettags(item):
        Scores = Scores[0:]+' 9'
        shotScores.configure(text = Scores)
        Total[1]+= 9
        totalScore.configure(text = Total)

    else:
        Scores = Scores[0:]+' 0'
        shotScores.configure(text = Scores)
        Total[1]+= 0
        totalScore.configure(text = Total)



print('#'*59+'\n\nLeft-click to shoot an arrow.\n\n'+'#'*59)
canvas.bind('<Button-1>', shotTaken)

Scores = 'Scores:'
shotScores = tk.Label(win, text=Scores)
shotScores.pack()

Total = ['Total:', 0]
totalScore = tk.Label(win, text=Total)
totalScore.pack()

quitButton = tk.Button(win, text='Quit game', command=win.destroy)
quitButton.pack()

win.mainloop()

#======================================
