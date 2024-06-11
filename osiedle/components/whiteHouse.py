import lib.move


def whiteHouse(t, x, y, w, h, overhangWidth):
    lib.move.move(t, x, y)
    t.goto(x+w, y)
    lib.move.move(t, x-overhangWidth, y+h)
    t.goto(-37.5, 50)
    t.goto(-50, 62.5)
    t.goto(-100, 62.5)
    t.goto(-112.5, 50)
