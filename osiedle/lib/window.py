import lib.square


def drawWindow(t, x, y):
    lib.square.drawSquare(t, x, y, 0.25, 0.25, "blue")
    lib.move.move(t, x, y + 6)
    t.goto(x + 12, y + 6)
    lib.move.move(t, x + 6, y)
    t.goto(x + 6, y + 12)
