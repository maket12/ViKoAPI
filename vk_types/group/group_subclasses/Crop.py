class Crop:
    def __init__(self, x: int, y: int, x2: int, y2: int):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

    def to_dict(self) -> dict:
        """Returns the crop object as a dictionary."""
        return {
            "x": self.x,
            "y": self.y,
            "x2": self.x2,
            "y2": self.y2
        }
