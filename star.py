import turtle

ati = turtle.Turtle()
#background color
ati.getscreen().bgcolor("#D55589")
ati.pensize(2)
ati.color("#50D8E2")

#think abt the angle ex:pentagon

#for i in range(5): #alt key ad selecting can comment multiple lines
#    ati.forward(10)
#    ati.left(216)

#change location
ati.penup()
ati.goto((-200,100))
ati.pendown()

def star(turtle,size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)

star(ati, 360)


turtle.exitonclick()