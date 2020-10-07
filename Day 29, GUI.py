#Day 29

import tkinter as tk
import tkinter.messagebox as tkm
from tkinter import ttk

#======================================It's GUI Time======================================
"""
window = tk.Tk()                            #Creates an application window
my_label = tk.Label(window, text='My GUI')  #Create a window label
my_label.pack()                             #Fits the size of the window to the label

def show_info():
    tkm.showinfo('Information', 'Thank you for running my program.')
    
def show_error():
    tkm.showerror('Error', 'An error has occurred!')
    
def show_warning():
    tkm.showwarning('Warning', 'You have been warned.')

my_canvas = tk.Canvas(window, width=300, height=200)  #Canvas lets you draw in the window
my_canvas.pack()
my_canvas.create_line(0,0,300, 200, fill='blue', width=3)
my_canvas.create_rectangle(10, 10, 200, 100, fill='red', outline='black', width=3)


def draw_rectangle():
    my_canvas.create_rectangle(20, 20, 190, 90, fill='blue', outline='black', width=3)


draw_button = tk.Button(window, text='Draw a rectangle!')
draw_button.pack()
draw_button['command'] = draw_rectangle


quit_button = tk.Button(window, text='Quit')
quit_button.pack()
quit_button['command'] = window.destroy     #Index brackets to use for a dictionary
#NOTE: WINDOW.DESTROY IS A FUNCTION THAT DOES NOT REQUIRE A ()
#Also, you can place the command attribute of a widget directly in the assigning of a variable, or with brackets next to the variable
#ex: quit_button = tk.Button(window, text='Quit', command=window.destroy)


window.mainloop()    #Starts the GUI event loop
"""
#===================================Practice Problems=================================

#Number 1: Smiley Face

window = tk.Tk()                            #Creates an application window
my_label = tk.Label(window, text='My GUI')  #Create a window label
my_label.pack() 

my_canvas = tk.Canvas(window, width=300, height=300)  #Canvas lets you draw in the window
my_canvas.pack()
def createface():
    my_canvas.create_oval(50, 50, 250, 250, width=3, fill='yellow')
    my_canvas.create_oval(100, 100, 120, 120, width=3, fill='black')
    my_canvas.create_oval(180, 100, 200, 120, width=3, fill='black')
    my_canvas.create_arc(90,120,210,220, style='pieslice', fill='white', start=180, extent=180, width=3)

draw_button = tk.Button(window, text='Have your own personal smiley face!',command = createface)
draw_button.pack()

quit_button = tk.Button(window, text='Quit', command = window.destroy)
quit_button.pack()
