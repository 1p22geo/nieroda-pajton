import turtle
import utils.constants


def drawSquare(t: turtle.Turtle, x, y, w, h, c):
    t.penup()
    t.goto(x, y)
    t.pendown()
    if c:
        t.fillcolor(c)
        t.begin_fill()
    t.goto(
        x,
        y +
        utils.constants.SettingsSingleton.settings["units"]["sigma"]["pixel"] *
        h)
    t.goto(
        x +
        utils.constants.SettingsSingleton.settings["units"]["sigma"]["pixel"] *
        w,
        y +
        utils.constants.SettingsSingleton.settings["units"]["sigma"]["pixel"] *
        h)
    t.goto(
        x +
        utils.constants.SettingsSingleton.settings["units"]["sigma"]["pixel"] *
        w,
        y)
    t.goto(x, y)
    if c:
        t.end_fill()
