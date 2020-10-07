#2/13/2019 In-class practice
import turtle
#Compound Interest
P = float(input("How much money did you initially invest? (no commas) "))
r = float(input("What was the compound interest rate? (in percentage) "))
r = r / 100 #changing from percentage to decimal
n = int(input("How many compoundings are there per year? "))
t = int(input("How many years will your investment grow? "))
A = int(P*(1+(r/n))**(n*t))
print("Your investment will end up being",A,"dollars.")

#How Old?
name = str(input("What is your name? "))
age = int(input("How old are you? "))
YrsTil = int(100 - age)
FinalYr = int(2019 + YrsTil)
print("Hello, "+str(name)+" you will 100 years old in "+str(FinalYr)+".")

#Turtle Square
wn = turtle.Screen()
Jack = turtle.Turtle()
Jack.width(5)
Jack.color("blue")
Jack.fillcolor("orange")
Jack.begin_fill()
Jack.forward(90)
Jack.left(90)
Jack.forward(90)
Jack.left(90)
Jack.forward(90)
Jack.left(90)
Jack.forward(90)
Jack.left(90)
Jack.end_fill()
