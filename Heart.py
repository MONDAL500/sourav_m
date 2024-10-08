import turtle

t = turtle.Turtle()
#s = turtle.Turtle()
wn = turtle.Screen()
wn.title("SOURAV MONDAL")
wn.bgcolor("white")
#t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color("red")
t.begin_fill()
t.left(148)
t.forward(155)
t.circle(-90,200)
t.setheading(59)
t.circle(-90,200)
t.forward(155)
t.end_fill()

#t.penup()

t.goto(-130,130)
#t.pndown()
t.color("White")
t.write("Love you KARTIK",font=("verdana",20,"bold"))
t.hideturtle()

turtle.done()