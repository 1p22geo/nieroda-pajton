import turtle

import lib.square
import lib.door
import lib.window
import lib.move
import lib.roof

import components.whiteHouse
import components.parking
import components.plac

from components.parking.parkingConfig import ParkingConfig
from funcs.asyncRoadBlock import asyncRoadBlock
import utils.rusztowanie.customRusztowanie.customRusztowanie
import utils.drogaKreski

from threaded_turtle import ThreadSerializer, TurtleThread

ctrl = ThreadSerializer()

t = turtle.Turtle()


# Droga i domki
TurtleThread(ctrl, turtle.Turtle(), target=asyncRoadBlock).start()


ctrl.run_forever(1)
# Drzwi
lib.door.drawDoor(t, -207.5, 0)
lib.door.drawDoor(t, -157.5, 0)
lib.door.drawDoor(t, -7.5, 0)
lib.door.drawDoor(t, 67.5, 0)

# Okna
lib.window.drawWindow(t, -217.5, 30)
lib.window.drawWindow(t, -142.5, 42.5)
lib.window.drawWindow(t, 6, 42.5)
lib.window.drawWindow(t, -18, 42.5)
lib.window.drawWindow(t, 6, 67.5)
lib.window.drawWindow(t, -18, 67.5)
lib.window.drawWindow(t, 100, 15)

# Dachy
lib.roof.drawRoof(t, -225, 50, 50, 25)
lib.roof.drawRoof(t, -175, 75, 50, 25)

# Bialy domek
components.whiteHouse.whiteHouse(t, -100, 35, 50, 15, 12.5)
# parking
components.parking.Parking(t, 110, -35, ParkingConfig())

# Plac z fontanna
components.plac.plac(t, -90, -35)
# Droga wypelnienie
lib.square.drawSquare(t, -250, 0, 10, -0.5, "grey")
lib.square.drawSquare(t, -125, -25, 0.5, -3.5, "grey")
lib.square.drawSquare(t, 75, -25, 0.5, -3.5, "grey")

# Droga kreski
utils.drogaKreski.drogaKreski(t, -250, -12.5)
# Custom rusztowanie
utils.rusztowanie.customRusztowanie.customRusztowanie.customRusztowanie(
    t, 50, 40)
turtle.mainloop()
