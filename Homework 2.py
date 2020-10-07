###Ethan Brinkman
###Homework 2, problems: 7, 8, 10, 12
###Due 2/15/2019

#Number 7
P = int(10000)
r = float(8)
r = r / 100 #changing from percentage to decimal
n = int(12)
t = int(input("How many years will your $10,000 investment grow? "))
A = int(P*(1+(r/n))**(n*t))
print("With 12 compounds per year, your $10,000 investment will be",A,"dollars.\n")


#Number 8
r = float(input("What is the radius of your circle? "))
A = round(((r**2)*3.14159),2)
print("Your circle has an area of",A,"square units.\n")

#Number 10
M = float(input("How many miles have you driven? "))
G = float(input("How many gallons of gas did you use? "))
print("Your MPG is "+str(round((M/G),1))+".\n")

#Number 12
F = float(input("What's the temperature outside? (in degrees Farenheit) "))
C = float(round((F-32)*(5/9),1))
if F<=32:
    print("Brrr, that's cold; it's also about",C," degrees celsius.")
else:
    print("Cool beans. That temperature is about",C,"degrees celsius.")
