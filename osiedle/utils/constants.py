import utils.parseConstants


class SettingsSingleton():
    settings: dict

    def __init__(self):
        pass


SettingsSingleton.settings = utils.parseConstants.parseConstants()
