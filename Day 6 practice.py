#Day 6
#2/20/2019
import math
import random
import turtle

#Number 1
print("Problem 1\n")

h = 5
w = 2
def areaOfRectangle(height, width):
    area = height * width
    return area

print (areaOfRectangle(h,w))

#Number 2
print("\nProblem 2\n")

def roll_sum(n):
    sum = 0
    for i in range(n):
        roll = random.randrange(1,7)
        print(roll)
        sum+=roll
    return sum
print(roll_sum(10))

#Nmber 3
print("\nNumber 3\n")

def drawpolygon(s,l):
    wn = turtle.Screen()
    me = turtle.Turtle()
    me.shape("turtle")
    me.speed(10)
    me.fillcolor("pink")
    me.begin_fill()
    for i in range(s):
        me.forward(l)
        me.left(360/sides)
    me.end_fill()

sides = int(input("How many sides will your polygon have?\n"))
length = int(input("How long will each side be?\n"))
drawpolygon(sides,length)
