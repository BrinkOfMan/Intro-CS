###Ethan Brinkman
###Homework 5: Problems 1, 2, 8, 10, sumTo()
###Due 2/22/2019

import math
import time
import turtle

def reset(turt):
    turt.reset()
    turt.pensize(3)
    turt.color("hotpink")
    turt.speed(10)

#Number 1

print("Number 1")

def drawSquare(turt, leng): #This function uses the paramaters turt(le) and leng(th) to draw a square

    for i in range(4):
        turt.fd(leng)
        turt.left(90)

wn = turtle.Screen()       
wn.bgcolor("lightgreen")

me = turtle.Turtle()     
me.color("hotpink")
me.speed(10)
me.pensize(3)

for i in range(5):
    drawSquare(me, 20)   
    me.up()
    me.forward(40)       
    me.down()

time.sleep(1.5)
reset(me)

#Number 2

print("\nNumber 2\n")

def squareSequence(turt,lengt):
    
    for i in range(4):
        turt.fd(lengt)
        turt.left(90)
    me.up()
    me.fd(-10)
    me.right(90)
    me.fd(10)
    me.left(90)
    me.down()

        
total = 0

for i in range(5):
    total+=20
    squareSequence(me,total)

time.sleep(1.5)    
reset(me)

#Number 8

print("Number 8\n")

def areaOfCircle(r):
    area = math.pi*(r**2)
    return area

radius = float(input("What is the radius of your circle?\n"))
print(round(areaOfCircle(radius),3),"is the area of your circle.")

#Number 10

print("\nNumber 10\n")

def drawStar(t):
    for i in range(5):
        t.fd(100)
        t.left(216)
        
for i in range(5):
    drawStar(me)
    me.up()
    me.fd(350)
    me.right(144)
    me.down()

time.sleep(1.5)
turtle.bye()

#sumTo()

print("sumTo() problem\n")
def sumTo(n):
    Sum = 0
    for i in range(n):
        Sum += (i+1)
    return(Sum)

sumTo(3)
result = sumTo(int(input("How many numbers will be summed up?\n")))
print(result,"is the sum of all integers up to that number.")

input()                     #This is to prevent a cmd window from closing immediately

