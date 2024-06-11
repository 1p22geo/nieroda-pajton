import lib.move


def drawDoor(t, x, y):
    lib.move.move(t, x, y)
    t.fillcolor("red")
    t.begin_fill()
    t.goto(x, y + 20)
    t.goto(x + 15, y + 20)
    t.goto(x + 15, y)
    t.end_fill()
    lib.move.move(t, x + 10, y + 10)
    t.circle(1.5)
