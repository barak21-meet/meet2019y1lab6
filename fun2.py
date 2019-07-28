import turtle
turtle.goto(0,0)

turtle.direction=None

def up():
    turtle.direction="Up"
    print("You pressed the up key")
    on_move()
    

turtle.onkey(up, "Up")
turtle.listen()

def on_move():
    p=turtle.pos()

    if turtle.direction=="Up":
        turtle.forward(50)

    if turtle.direction=="Down":
        turtle.forward(50)

    if turtle.direction=="Left":
        turtle.forward(50)
    if turtle.direction=="Right":
        turtle.forward(50)
