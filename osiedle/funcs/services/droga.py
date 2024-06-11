import lib.square
import utils.drogaKreski


def asyncDroga(t):
    lib.square.drawSquare(t, -250, 0, 10, -0.5, "grey")
    lib.square.drawSquare(t, -125, -25, 0.5, -3.5, "grey")
    lib.square.drawSquare(t, 75, -25, 0.5, -3.5, "grey")

    utils.drogaKreski.drogaKreski(t, -250, -12.5)
