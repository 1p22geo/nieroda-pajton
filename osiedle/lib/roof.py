import lib.move


def drawRoof(t, x, y, w, h, color="red"):
    lib.move.move(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x+1/2*w, y+h)
    t.goto(x+w, y)
    t.end_fill()
