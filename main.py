import turtle  #https://docs.python.org/3/library/turtle.html #https://www.youtube.com/watch?v=8DEHcYvesXY
wn= turtle.Screen()

ati = turtle.Turtle()

ati.pensize(3)
ati.color("blue", "yellow")#orange/blue/red/cyan #https://www.colorspire.com/

#to make a SQUARE
ati.begin_fill()

ati.forward(100) #num within bracket is the radius
ati.left(90)      #90 degree
ati.forward(100)  #shortform left=lt, right=rt, forward=fd, backward=bk
ati.left(90)   #enter coordinates= ati.goto(100,100)
ati.forward(100) #bring turtle back to its home position= ati.home()
ati.left(90)
ati.forward(100)

ati.penup() #to make a space between squares
ati.forward(150)
ati.pendown()

ati.forward(100)
ati.left(90)
ati.forward(100)
ati.left(90)
ati.forward(100)
ati.left(90)
ati.forward(100)

ati.end_fill()

#to make a CIRCLE
#ati.circle(60)
#ati.dot(20) #fill in circle



turtle.exitonclick()