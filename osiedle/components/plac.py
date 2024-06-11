import lib.square
import lib.move


def plac(t, x, y):
    lib.square.drawSquare(t, x, y, 3.1, -3.1, "white")
    lib.move.move(t, x+80, y-105)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    base = {
        "x": x+80,
        "y": y-80
    }

    lib.move.move(t, base["x"], base["y"]-40)
    t.circle(40)
    lib.move.move(t, base["x"], base["y"])
    t.goto(-10, -75)
    lib.move.move(t, base["x"]+40, base["y"])
    t.left(90)
    t.circle(20, 180)
    lib.move.move(t, base["x"], base["y"])
    t.left(180)
    t.circle(20, 180)
