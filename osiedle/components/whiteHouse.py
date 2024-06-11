import lib.move


def whiteHouse(t, x, y, w, h, overhang):
    lib.move.move(t, x, y)
    t.goto(x + w, y)
    lib.move.move(t, x - overhang, y + h)
    t.goto(x + w + overhang, y + h)
    t.goto(x + w, y + h + overhang)
    t.goto(x, y + h + overhang)
    t.goto(x - overhang, y + h)
