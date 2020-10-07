#Day 5 In-class practice

import math
import random
import turtle

#1
wn = turtle.Screen()
me = turtle.Turtle()
me.shape("turtle")
a = random.randrange(20,201)
for i in range(6):
    me.fd(a)
    me.left(360/6)

#2
a = random.random()
print(a)
b = random.random()
print(b)
c = random.random()
print(c)
print("The sum of these random float points is",a+b+c)

#3
r = float(input("What is the radius of your circle?\n"))
print("The circumference is",math.pi*r*2)
print("The area is",math.pi*(r**2))

