###Ethan Brinkman
###Homework 4, problems: 16, 17, 18, and Triangle
###Due 2/20/2019

import random
import math

def main():
    
    #Number 16
    print("\nNumber 16:\n")
    
    amnt = 10
    for i in range(amnt):
        num = random.random()
        print(num)
        
    #Number 17
    print("\nNumber 17:\n")

    for i in range(amnt):
        num = random.randrange(25,36)
        print(num)

    #Number 18
    print("\nNumber 18:\n")

    a = float(input("How long is side a of your right triangle?\n"))
    b = float(input("How long is side b of your right triangle?\n"))
    c = round(math.hypot(a,b),3)
    print("The hypotenuse of your right triangle is",c)

    #Triangle problem
    print("\nTriangle Problem:\n")

    a = float(input("How long is side a of your triangle?\n"))
    b = float(input("How long is side b of your triangle?\n"))
    theta = float(input("What is the angle at where lines a and b meet?\n"))

    c = round(math.sqrt((a*a)+(b*b)-(2*a*b*math.cos(math.radians(theta)))),3)
    print("The remaining line is",c,"units long.")
    input() #This is just so the program won't immediately close after being ran in a cmd window
main()
