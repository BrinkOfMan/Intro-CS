###Ethan Brinkman
###Homework 3, problems: 4, 6, 7, 10, 12
##Due 2/18/2019

import math
import turtle
import random
import time

#Number 4

for num in [12, 10, 32, 3 ,66, 17, 42, 99, 20]:
    print(num)                                                              #Printing the current iteration
    square = math.sqrt(num)                                                 #Squaring the current iteration
    roundsquare = round(square, 3)                                          #Rounding the square to 3 sig. figs
    print(str(roundsquare) + " is the square root of " + str(num) + ".")    #Concating the strings of everything

#Number 6

sides = int(input("How many sides will you have in your polygon?\n"))
length = float(input("How long will each side be?\n"))
color = str(input("What color do you want to fill the polygon with?\n"))
turn = 360 / sides                                                          #Angle needed to complete the polygon for the desired sides

wn = turtle.Screen()
poly = turtle.Turtle()
poly.shape("turtle")
poly.fillcolor(color)
poly.begin_fill()

for i in range(sides):
    poly.fd(length)
    poly.left(turn)
    
poly.end_fill()

#Number 7

#This is for fun, it doesn't really pertain to number 7. I put this chunk in problem 7 just to separate my train of thought

time.sleep(1)
response = str(input("Are you done looking at your wonderful polygon? y / n\n"))
if response == "n":
    time.sleep(2)
    response2 = str(input("Now are you done looking at your wonderful polygon? y / n\n"))
    if response2 == "n":
        print("Well...")
        time.sleep(2)
        print("I am.")
        time.sleep(3)
        print("So let's move on.")
        time.sleep(1)
        wn.reset()
    else:
        print("Okay. let's move on, then.")
        wn.reset()
else:
        print("Okay. let's move on, then.")
        wn.reset()
        
#Number 7 starts now

pirate = poly
pirate.shape("classic")
print("\nWoah, there's a drunk pirate walking around and leaving a trail behind him!\n")
for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(i)
    pirate.forward(100)
print("The pirate ended with a heading position of" , pirate.heading())
time.sleep(1.5)
wn.reset()

#Number 10

me = pirate
me.shape("turtle")
me.color("blue")
wn.bgcolor("lightgreen")
me.width(3)
angle = 360 // 12

for i in range(12):
    me.right(angle)
    me.up()
    me.fd(70)
    me.down()
    me.fd(7)
    me.up()
    me.fd(20)
    me.stamp()
    me.back(97)

#Number 12
print("The assigned variable turtle type is",type(me))
input()
