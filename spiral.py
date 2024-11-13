import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(400,300)
colors=["Blue","Red","Green","orange"]
board=turtle.Turtle()
board.hideturtle()
while True:
    for x in range (200):
        board.pencolor(colors[x%len(colors)])
        board.width(x/100+1)
        board.forward(x)
        board.left(59)
    board.right(239)

