import lib.door

import time


def asyncDrzwi(t):
    time.sleep(10)
    lib.door.drawDoor(t, -207.5, 0)
    lib.door.drawDoor(t, -157.5, 0)
    lib.door.drawDoor(t, -7.5, 0)
    lib.door.drawDoor(t, 67.5, 0)
