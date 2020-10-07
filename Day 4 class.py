#Day 4 class stuff
#for <item> in <list>:
#   print(item)
#print("loop done.")

#convention in computer science to use "i" as the default for(): variable
import turtle
wn = turtle.Screen()
me = turtle.Turtle()
me.shape("circle")
me.speed(250)
me.hideturtle()
me.up()
me.goto(-150,-200)
me.down()
for i in range(0,360,1):
    me.fd(250)
    me.left(61)
wn.exitonclick()

