from threaded_turtle import ThreadSerializer, TurtleThread
import turtle

from main.functors import \
    asyncRoadBlock, \
    asyncDrzwi, \
    asyncOkna, \
    asyncDachy, \
    asyncWhiteHouse, \
    asyncParking, \
    asyncPlac, \
    asyncDroga, \
    asyncRusztowanie


ctrl = ThreadSerializer()


threads = [
    TurtleThread(ctrl, turtle.Turtle(), target=asyncRoadBlock),
    TurtleThread(ctrl, turtle.Turtle(), target=asyncDrzwi),
    TurtleThread(ctrl, turtle.Turtle(), target=asyncOkna),
    TurtleThread(ctrl, turtle.Turtle(), target=asyncDachy),
    TurtleThread(ctrl, turtle.Turtle(), target=asyncWhiteHouse),
    TurtleThread(ctrl, turtle.Turtle(), target=asyncParking),
    TurtleThread(ctrl, turtle.Turtle(), target=asyncPlac),
    TurtleThread(ctrl, turtle.Turtle(), target=asyncDroga),
    TurtleThread(ctrl, turtle.Turtle(), target=asyncRusztowanie)
]
