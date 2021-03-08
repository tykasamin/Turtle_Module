import turtle
import math

ati = turtle.Turtle()
ati.pensize(5)
ati.color("purple", "cyan")
ati.speed(10)

ati.begin_fill()
#for i in range(100):
#    ati.forward(300)
#    ati.left(170)
#using math function
for i in range(2000):
   ati.forward(10)
   ati.left(math.sin(i/10)*25)
   ati.left(20)

ati.end_fill()

turtle.exitonclick()