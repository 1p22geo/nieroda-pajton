import turtle

import lib
import lib.square
import lib.door
import lib.window
import lib.move
import lib.roof

import components.whiteHouse
import components.parking


t = turtle.Turtle()
t.speed(100000000000)


# Droga i domki
lib.square.drawSquare(t, -225, 0, 1, 1, "yellow")
lib.square.drawSquare(t, -175, 0, 1, 1.5, "yellow")
lib.square.drawSquare(t, -100, 0, 1, 1, "white")
lib.square.drawSquare(t, -25, 0, 1, 2, "green")
lib.square.drawSquare(t, 50, 0, 2, 1, "yellow")
lib.square.drawSquare(t, -100, -25, 3.5, -3.5, "white")

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
components.parking.Parking(t, 110, -35)

# Plac z fontanna
lib.square.drawSquare(t, -90, -35, 3.1, -3.1, "white")
lib.move.move(t, -10, -140)
t.fillcolor("blue")
t.begin_fill()
t.circle(25)
t.end_fill()
lib.move.move(t, -10, -155)
t.circle(40)
lib.move.move(t, -10, -115)
t.goto(-10, -75)
lib.move.move(t, 30, -115)
t.left(90)
t.circle(20, 180)
lib.move.move(t, -10, -115)
t.left(180)
t.circle(20, 180)

# Droga wypelnienie
lib.square.drawSquare(t, -250, 0, 10, -0.5, "grey")
lib.square.drawSquare(t, -125, -25, 0.5, -3.5, "grey")
lib.square.drawSquare(t, 75, -25, 0.5, -3.5, "grey")

# Droga kreski
lib.move.move(t, -250, -12.5)
t.goto(-230, -12.5)
lib.move.move(t, -210, -12.5)
t.goto(-190, -12.5)
lib.move.move(t, -170, -12.5)
t.goto(-150, -12.5)
lib.move.move(t, -130, -12.5)
t.goto(-110, -12.5)
lib.move.move(t, -90, -12.5)
t.goto(-70, -12.5)
lib.move.move(t, -50, -12.5)
t.goto(-30, -12.5)
lib.move.move(t, -10, -12.5)
t.goto(10, -12.5)
lib.move.move(t, 30, -12.5)
t.goto(50, -12.5)
lib.move.move(t, 70, -12.5)
t.goto(90, -12.5)
lib.move.move(t, 110, -12.5)
t.goto(130, -12.5)
lib.move.move(t, 150, -12.5)
t.goto(170, -12.5)
lib.move.move(t, 190, -12.5)
t.goto(210, -12.5)
lib.move.move(t, 230, -12.5)
t.goto(250, -12.5)
lib.move.move(t, -112.5, -25)
t.goto(-112.5, -45)
lib.move.move(t, -112.5, -65)
t.goto(-112.5, -85)
lib.move.move(t, -112.5, -105)
t.goto(-112.5, -125)
lib.move.move(t, -112.5, -145)
t.goto(-112.5, -165)
lib.move.move(t, -112.5, -185)
t.goto(-112.5, -205)
lib.move.move(t, 87.5, -25)
t.goto(87.5, -45)
lib.move.move(t, 87.5, -65)
t.goto(87.5, -85)
lib.move.move(t, 87.5, -105)
t.goto(87.5, -125)
lib.move.move(t, 87.5, -145)
t.goto(87.5, -165)
lib.move.move(t, 87.5, -185)
t.goto(87.5, -205)

# Custom rusztowanie
lib.move.move(t, 50, 40)
t.goto(150, 40)
t.goto(140, 40)
t.goto(140, 0)
t.goto(130, 0)
t.goto(130, 40)
lib.move.move(t, 50, 40)
t.circle(5, 180)
lib.move.move(t, 60, 40)
t.right(180)
t.circle(5, 180)
lib.move.move(t, 70, 40)
t.right(180)
t.circle(5, 180)
lib.move.move(t, 80, 40)
t.right(180)
t.circle(5, 180)
lib.move.move(t, 90, 40)
t.right(180)
t.circle(5, 180)
lib.move.move(t, 100, 40)
t.right(180)
t.circle(5, 180)
lib.move.move(t, 110, 40)
t.right(180)
t.circle(5, 180)
lib.move.move(t, 120, 40)
t.right(180)
t.circle(5, 180)
lib.move.move(t, 130, 40)
t.right(180)
t.circle(5, 180)
lib.move.move(t, 140, 40)
t.right(180)
t.circle(5, 180)

turtle.mainloop()
