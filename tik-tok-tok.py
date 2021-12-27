import turtle
wx=turtle.Screen()
a=turtle.Turtle()
a.color("black")
a.width(2)
a.speed(2)
for i in range(4):
    a.forward(300)
    a.left(90)
#for inner line
a.penup()
a.goto(0,100)
a.pendown()
a.forward(300)

a.penup()
a.goto(0,200)
a.pendown()
a.forward(300)

a.penup()
a.goto(100,0)
a.pendown()
a.left(90)
a.forward(300)

a.penup()
a.goto(200,0)
a.pendown()
a.forward(300)
