import components.whiteHouse
import time
import utils.constants


def asyncWhiteHouse(t):
    # async timeout for component functor to sync effect callbacks
    time.sleep(
        2 * utils.constants.SettingsSingleton.settings["threading"]["syncDelayUnit"])

    components.whiteHouse.whiteHouse(t, -100, 35, 50, 15, 12.5)
