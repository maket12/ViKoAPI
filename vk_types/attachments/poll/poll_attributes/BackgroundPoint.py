class BackgroundPoint:
    def __init__(self, position: int, color: str):
        self.position = position
        self.color = color

    def to_dict(self) -> dict:
        """Returns the polls background gradient point object as a dictionary."""
        return {
            "position": self.position,
            "color": self.color
        }
