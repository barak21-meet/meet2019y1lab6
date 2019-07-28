
import turtle
turtle.tracer(1)
rounds = 10
size = 10
mike = turtle.clone()
steve = turtle.clone()
turtle.bgcolor("white")
turtle.hideturtle()
mike.color("gold")
steve.color("blue")
steve.goto(5,5)
while True:
    mike.forward(size)
    mike.left(90)
    steve.forward(-size)
    steve.left(-90)
    size += 10
turtle.mainloop()
