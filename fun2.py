import turtle
turtle.goto(0,0)

turtle.direction=None

def up():
    turtle.direction="Up"
    print("You pressed the up key")
    on_move()
    

turtle.onkey(up, "Up")
turtle.listen()


def down():
    turtle.direction="Down"
    print("You pressed the down key")
    on_move()

turtle.onkey(down, "Down")
turtle.listen()

def left():
    turtle.direction="Left"
    print("You pressed the left key")
    on_move()

turtle.onkey(left, "Left")
turtle.listen()

def right():
    turtle.direction="Right"
    print("You pressed the right key")
    on_move()

turtle.onkey(right, "Right")
turtle.listen()

def space():
    turtle.penup()

    
turtle.onkey(space, "space")
turtle.listen()

def c():
    turtle.pendown()

turtle.onkey(c, "c")
turtle.listen()
    
def on_move():
    p=turtle.pos()


    if turtle.direction=="Up":
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)

    if turtle.direction=="Down":
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)

    if turtle.direction=="Left":
        turtle.right(180)
        turtle.forward(50)
        turtle.left(180)
    if turtle.direction=="Right":
        turtle.forward(50)
