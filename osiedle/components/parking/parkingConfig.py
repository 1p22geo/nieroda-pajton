class ParkingConfig():
    size: int
    """
        The size of a single parking lot. Alias for blockSize
    """
    blockSize: int
    """
        The size of a single parking lot.
    """

    def __init__(self, blockSize=45, distance=115, circleRadius=25, font="Arial") -> None:
        self.blockSize = blockSize
        self.distance = distance
        self.circleRadius = circleRadius
        self.font = font

        @property
        def size(self):
            return self.blockSize

        @size.setter
        def size(self, value):
            self.size = value

        @size.deleter
        def size(self):
            del self.size
