import turtle

from funcs.asyncRoadBlock import asyncRoadBlock
from funcs.asyncDrzwi import asyncDrzwi
from funcs.asyncOkna import asyncOkna
from funcs.asyncDachy import asyncDachy

from funcs.components.asyncWhiteHouse import asyncWhiteHouse
from funcs.components.asyncParking import asyncParking

from funcs.services.plac import asyncPlac
from funcs.services.droga import asyncDroga
from funcs.services.rusztowanie import asyncRusztowanie

from threaded_turtle import ThreadSerializer, TurtleThread

ctrl = ThreadSerializer()

t = turtle.Turtle()


TurtleThread(ctrl, turtle.Turtle(), target=asyncRoadBlock).start()
TurtleThread(ctrl, turtle.Turtle(), target=asyncDrzwi).start()
TurtleThread(ctrl, turtle.Turtle(), target=asyncOkna).start()
TurtleThread(ctrl, turtle.Turtle(), target=asyncDachy).start()
TurtleThread(ctrl, turtle.Turtle(), target=asyncWhiteHouse).start()
TurtleThread(ctrl, turtle.Turtle(), target=asyncParking).start()
TurtleThread(ctrl, turtle.Turtle(), target=asyncPlac).start()
TurtleThread(ctrl, turtle.Turtle(), target=asyncDroga).start()
TurtleThread(ctrl, turtle.Turtle(), target=asyncRusztowanie).start()


ctrl.run_forever(10)
