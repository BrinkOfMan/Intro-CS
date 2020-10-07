#Day 8
import random

#Any variable is true to the if statement except 0
#This is useful for things like
#And/Or/Not evaluates everything given as true or false before returning the boolean value


x = random.randrange(0,5)
y = random.randrange(0,5)

print("x is",x)
print("y is",y)

if x and y:
    print(y/x)
elif(not(x or y)):
    print("x and y are false")
elif(x):
    print("y is false")
else:
    print("x is false")
