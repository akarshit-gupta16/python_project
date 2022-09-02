#Tri-colour without spokes
import turtle
length = eval(input("Enter the total length of the tri colour:"))
width = eval(input("Enter the total width of the tri colour:"))
tri = turtle.Turtle()

#*******************************************
def orange(l, b):
    tri.setheading(180)
    tri.begin_fill()
    tri.fillcolor("orange")
    for i in range(4):
        if i % 2 == 0:
            tri.forward(l)
            tri.right(90)

        else:
            tri.forward(b)
            tri.right(90)
    tri.end_fill()


def white(l, b):
    for i in range(4):
        if i % 2 == 0:
            tri.forward(l)
            tri.left(90)

        else:
            tri.forward(b)
            tri.left(90)


def green(l, b):
    tri.setheading(270)
    tri.forward(2*b)
    tri.right(90)
    tri.begin_fill()
    tri.fillcolor("green")
    for i in range(4):
        if i % 2 == 0:
            tri.forward(l)
            tri.right(90)
        else:
            tri.forward(b)
            tri.right(90)
    tri.end_fill()
#*************************************************************


width = width//3
tri.hideturtle()

orange(length, width)
white(length, width)
green(length, width)
turtle.done()
