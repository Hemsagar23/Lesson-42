import turtle

turtle.Screen().bgcolor("Red")

sc = turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()
board.speed(10)

for i in range(500):
    board.shape("turtle")
    board.forward(100)
    board.left(305)
    i= i + 1
    
turtle.done()