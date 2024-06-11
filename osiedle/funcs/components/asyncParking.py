import components.parking
import utils.constants
from components.parking.parkingConfig import ParkingConfig


def asyncParking(t):
    components.parking.Parking(
        t,
        110,
        -35,
        ParkingConfig(
            font=utils.constants.SettingsSingleton.settings["osVisuals"]["font"],
            fontSize=utils.constants.SettingsSingleton.settings["osVisuals"][
                "fontSize"
            ],
        ),
    )
