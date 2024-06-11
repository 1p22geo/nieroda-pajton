import lib.move
from components.parking.parkingConfig import ParkingConfig

# components.parking.Parking(110, -35)


class Parking:
    def __init__(self, t, x, y, config: ParkingConfig) -> None:
        self.x = x
        self.y = y
        self.t = t
        self.config = config
        self.gora()
        self.dol()
        self.kolo()

    def gora(self):
        t = self.t  # alias for tutel
        lib.move.move(t, self.x, self.y)

        t.goto(self.x, self.y - self.config.size)
        t.goto(self.x + self.config.size, self.y - self.config.size)
        t.goto(self.x + self.config.size, self.y)
        t.goto(self.x + self.config.size, self.y - self.config.size)
        t.goto(self.x + self.config.size * 2, self.y - self.config.size)
        t.goto(self.x + self.config.size * 2, self.y)
        t.goto(self.x + self.config.size * 2, self.y - self.config.size)
        t.goto(self.x + self.config.size * 3, self.y - self.config.size)
        t.goto(self.x + self.config.size * 3, self.y)
        lib.move.move(t, self.x, self.y)

    def dol(self):
        t = self.t
        y = self.y - self.config.distance
        lib.move.move(t, self.x, y)
        t.goto(self.x, y - self.config.size)
        t.goto(self.x, y)
        t.goto(self.x + self.config.size, y)
        t.goto(self.x + self.config.size, y - self.config.size)
        t.goto(self.x + self.config.size, y)
        t.goto(self.x + self.config.size * 2, y)
        t.goto(self.x + self.config.size * 2, y - self.config.size)
        t.goto(self.x + self.config.size * 2, y)
        t.goto(self.x + self.config.size * 3, y)
        t.goto(self.x + self.config.size * 3, y - self.config.size)

    def kolo(self):
        lib.move.move(
            self.t, self.x + self.config.size * 1.5, self.y -
            self.config.size - self.config.distance / 2
        )
        self.t.circle(self.config.circleRadius)
        self.litera()

    def litera(self):
        lib.move.move(self.t, self.x + self.config.size*1.5-10,
                      self.y - self.config.size - self.config.distance/2+13)
        self.t.color("black")
        self.t.write("P", font=(self.config.font, 20, "bold"))
