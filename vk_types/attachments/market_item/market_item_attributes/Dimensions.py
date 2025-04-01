class MarketItemDimensions:
    def __init__(self, width: int, height: int, length: int):
        self.width = width
        self.height = height
        self.length = length

    def to_dict(self) -> dict:
        """Returns the market item dimensions object as a dictionary."""
        return {
            "width": self.width,
            "height": self.height,
            "length": self.length
        }
