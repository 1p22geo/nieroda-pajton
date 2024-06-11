import components.whiteHouse
import time


def asyncWhiteHouse(t):
    # async timeout for component functor to sync effect callbacks
    time.sleep(10)
    components.whiteHouse.whiteHouse(t, -100, 35, 50, 15, 12.5)
