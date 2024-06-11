import lib.door

import utils.constants
import time


def asyncDrzwi(t):
    time.sleep(
        2 * utils.constants.SettingsSingleton.settings["threading"]["syncDelayUnit"])
    lib.door.drawDoor(t, -207.5, 0)
    lib.door.drawDoor(t, -157.5, 0)
    lib.door.drawDoor(t, -7.5, 0)
    lib.door.drawDoor(t, 67.5, 0)
