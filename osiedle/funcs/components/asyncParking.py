import components.parking
from components.parking.parkingConfig import ParkingConfig


def asyncParking(t):
    components.parking.Parking(t, 110, -35, ParkingConfig())
