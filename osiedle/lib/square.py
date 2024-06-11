import turtle


def drawSquare(t: turtle.Turtle, x, y, w, h, c):
    t.penup()
    t.goto(x, y)
    t.pendown()
    if c:
        t.fillcolor(c)
        t.begin_fill()
    t.goto(x, y + 50 * h)
    t.goto(x + 50 * w, y + 50 * h)
    t.goto(x + 50 * w, y)
    t.goto(x, y)
    if c:
        t.end_fill()
