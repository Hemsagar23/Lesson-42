import turtle

turtle.bgcolor("lightblue")
turtle.pensize(3)
turtle.speed(3)

turtle.color("red")
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

turtle.color("green")
turtle.fillcolor("orange")
turtle.begin_fill()
for i in range(2):
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.goto(400, 0)
turtle.pendown()

turtle.color("blue")
turtle.fillcolor("pink")
turtle.begin_fill()
for i in range(6):
    turtle.forward(80)
    turtle.left(60)
turtle.end_fill()

turtle.done()
