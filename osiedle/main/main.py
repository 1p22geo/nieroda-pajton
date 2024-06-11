from main.threads import ctrl, threads

import utils.constants


def main():
    for thread in threads:
        thread.setDaemon(True)
        thread.start()

    ctrl.run_forever(
        utils.constants.SettingsSingleton.settings["threading"]["threadTimeout"])
