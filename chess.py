import turtle
c=turtle.Turtle()
c.speed(0)
c.shape("turtle")
def draw_square1():
    for i in range(4):
        c.forward(40)
        c.left(90)
def draw_square2():
    for i in range(4):
        c.forward(40)
        c.right(90)

def chess_board1():
    for i in range(8):
        if i%2==0:
            c.begin_fill()
            c.fillcolor("black")
            draw_square1()
            c.end_fill()
            c.penup()
            c.forward(40)
            c.pendown()
        else:
            draw_square1()
            c.penup()
            c.forward(40)
            c.pendown()
    c.left(90)
    c.forward(40)
    c.left(90)
def chess_board2():
    for i in range(8):
        if i%2==0:
            c.begin_fill()
            c.fillcolor("black")
            draw_square2()
            c.end_fill()
            c.penup()
            c.forward(40)
            c.pendown()
        else:
            draw_square2()
            c.penup()
            c.forward(40)
            c.pendown()
    c.right(90)
    c.forward(40)
    c.right(90)
for i in range(4):
    chess_board1()
    chess_board2()
turtle.done()