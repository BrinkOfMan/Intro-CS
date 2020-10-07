#Day 3 lecture
import turtle
wn = turtle.Screen()
angle = 0
name="ore wa"
for name in range(0,15,1):
    print(name)
    name = turtle.Turtle()
    name.speed(100)
    name.shape("turtle")
    name.up()
    name.right(angle)
    name.forward(50)
    name.speed(2)
    name.forward(500)
    angle = angle + 24

 


