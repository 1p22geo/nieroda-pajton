import lib.move

# components.parking.Parking(110, -35)


class Parking():
    def __init__(self, t, x, y) -> None:
        self.x = x
        self.y = y
        self.t = t
        self.gora()
        self.dol()
        self.kolo()

    def gora(self):
        t = self.t  # alias for tutel
        lib.move.move(t, self.x, self.y)

        t.goto(self.x, self.y-45)
        t.goto(self.x+45, self.y-45)
        t.goto(self.x + 45, self.y)
        t.goto(self.x + 45, self.y-45)
        t.goto(200, self.y-45)
        t.goto(200, self.y)
        t.goto(200, self.y-45)
        t.goto(245, self.y-45)
        t.goto(245, self.y)
        lib.move.move(t, self.x, self.y)

        pass

    def dol(self):
        pass

    def kolo(self):
        self.litera()

    def litera(self):
        pass
