import lib.move

# components.parking.Parking(110, -35)


class Parking:
    def __init__(self, t, x, y, size=45, distance=115, circleRadius=25) -> None:
        self.x = x
        self.y = y
        self.t = t
        self.size = size
        self.distance = distance
        self.circleRadius = circleRadius
        self.gora()
        self.dol()
        self.kolo()

    def gora(self):
        t = self.t  # alias for tutel
        lib.move.move(t, self.x, self.y)

        t.goto(self.x, self.y - self.size)
        t.goto(self.x + self.size, self.y - self.size)
        t.goto(self.x + self.size, self.y)
        t.goto(self.x + self.size, self.y - self.size)
        t.goto(self.x + self.size * 2, self.y - self.size)
        t.goto(self.x + self.size * 2, self.y)
        t.goto(self.x + self.size * 2, self.y - self.size)
        t.goto(self.x + self.size * 3, self.y - self.size)
        t.goto(self.x + self.size * 3, self.y)
        lib.move.move(t, self.x, self.y)

    def dol(self):
        t = self.t
        y = self.y - self.distance
        lib.move.move(t, self.x, y)
        t.goto(self.x, y - self.size)
        t.goto(self.x, y)
        t.goto(self.x + self.size, y)
        t.goto(self.x + self.size, y - self.size)
        t.goto(self.x + self.size, y)
        t.goto(self.x + self.size * 2, y)
        t.goto(self.x + self.size * 2, y - self.size)
        t.goto(self.x + self.size * 2, y)
        t.goto(self.x + self.size * 3, y)
        t.goto(self.x + self.size * 3, y - self.size)

    def kolo(self):
        lib.move.move(
            self.t, self.x + self.size * 1.5, self.y - self.size - self.distance / 2
        )
        self.t.circle(self.circleRadius)
        self.litera()

    def litera(self):
        pass
