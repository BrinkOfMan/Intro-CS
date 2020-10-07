#Ethan Brinkman
#Homework 8: 2, 4, 5, 6
#Due 3/6/19

import random
import turtle
import time


#Number 2
print("Number 2\n")

def print_triangular_numbers(n):
    print("Loop #","\t","Triangular number")
    print("======","\t","=================")
    Sum = 0
    for i in range(n):
        i += 1
        Sum += i
        print(i,"\t",Sum)
        

print("The first 5 triangular numbers go as follow:\n")
print_triangular_numbers(5)


#Number 4
print("\nNumber 4\n")

wn = turtle.Screen()
leftBound = -(wn.window_width() / 2)
rightBound = wn.window_width() / 2
topBound = wn.window_height() / 2
bottomBound = -(wn.window_height() / 2)

#===========Code imported from section 8.4============
def isInScreen(wn,t):

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn
#=====================================================

#establishing turtle me
wn = turtle.Screen()
me = turtle.Turtle()
me.shape("turtle")
me.fillcolor("darkgreen")
me.width(2)
me.speed(7)

def randmove(t):
    direction = random.randrange(0, 2)
    if direction == 0:              
        t.left(random.randrange(1,181))
    else:                      
        t.right(random.randrange(1,181))

    t.forward(random.randrange(30,71))

while isInScreen(wn, me):
    randmove(me)

print("me has left the screen. Resetting window for number 5.")
time.sleep(2)
wn.reset()


#Number 5
print("\nNumber 5\n")

#Re-establishing turtle me and putting me at a random spot
me.fillcolor("darkgreen")
me.width(2)
me.speed(7)
me.up()
me.goto(random.randrange(leftBound/2, rightBound/2), random.randrange(bottomBound/2, topBound/2))
me.down()

#Establishing turtle you and putting you at a random spot
you = turtle.Turtle()
you.shape("turtle")
you.fillcolor("lightgreen")
you.width(2)
you.speed(7)
you.up()
you.goto(random.randrange(leftBound/2, rightBound/2), random.randrange(bottomBound/2, topBound/2))
you.down()

#Move the turtles
while isInScreen(wn, you) and isInScreen(wn, me):
    randmove(you)
    if isInScreen(wn, you):             #Only if you is in the screen will me move
        randmove(me)
print("A turtle has left the screen. Resetting window for number 6.")
time.sleep(2)
turtle.clearscreen()

#Number 6
print("\nNumber 6\n")

#Re-establishing turtle me and putting me at a random spot
me = turtle.Turtle()
me.shape("turtle")
me.fillcolor("darkgreen")
me.width(2)
me.speed(7)
me.up()
me.goto(random.randrange(leftBound/2, rightBound/2), random.randrange(bottomBound/2, topBound/2))
me.down()

#Establishing turtle you and putting you at a random spot
you = turtle.Turtle()
you.shape("turtle")
you.fillcolor("lightgreen")
you.width(2)
you.speed(7)
you.up()
you.goto(random.randrange(leftBound/2, rightBound/2), random.randrange(bottomBound/2, topBound/2))
you.down()

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

for i in range(50):                     #50 iterations of movement for both me and you
    if areColliding(me, you) == False and isInScreen(wn, you) == True:
        #If you and me are not colliding and you is in the screen, continue moving randomly.
        randmove(you)
    else:
        print("you either went out of the screen or bumped into me. Please turn around, you.\n")
        you.right(180)
        you.forward(111)
        
    if areColliding(me, you) == False and isInScreen(wn, me) == True:
        randmove(me)
    else:
        print("me either went out of the screen or bumped into you. Please turn around, me.\n")
        me.right(180)
        me.forward(111)

print("50 iterations complete. Goodbye.")    
time.sleep(2)
turtle.bye()

