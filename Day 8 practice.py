#Day 8 practice
import turtle

#Number 1

def percentage():
    
    decimalNum = float(input("Enter a decimal number\n"))
    if (decimalNum <= 1 and decimalNum >= 0):
        print("Your decimal is equal to "+str(decimalNum*100)+"%")
    else:
        print("Your entered a number that is not between 0 and 1")
percentage()

#Number 2

def drawthing():
    
    whatNum = int(input("Enter a number\n"))
    if whatNum == 0:
        wn = turtle.Screen()
        me = turtle.Turtle()
        me.shape("turtle")
        me.fillcolor("pink")
        me.begin_fill()
        me.width(3)
        for i in range(3):
            me.fd(60)
            me.left(120)
        me.end_fill()
    else:
        wn = turtle.Screen()
        me = turtle.Turtle()
        me.shape("turtle")
        me.fillcolor("pink")
        me.begin_fill()
        me.width(3)
        for i in range(4):
            me.fd(60)
            me.left(90)
        me.end_fill()
        
drawthing()
        
#Number 3

def largest():
    a = float(input("Enter a number\n"))
    b = float(input("Enter a second number\n"))
    c = float(input("Enter a third number\n"))
    bigboi = max(a,b,c)
    print(bigboi,"Is the largest of the three numbers entered.")

largest()
