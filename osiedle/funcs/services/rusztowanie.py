import utils.constants
import time
import utils.rusztowanie.customRusztowanie.customRusztowanie


def asyncRusztowanie(t):
    time.sleep(
        3 *
        utils.constants.SettingsSingleton.settings["threading"]["syncDelayUnit"]
    )

    utils.rusztowanie.customRusztowanie.customRusztowanie.customRusztowanie(
        t, 50, 40)
