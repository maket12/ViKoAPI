class Graffiti:
    def __init__(self, graffiti_id: int, owner_id: int, url: str, width: int, height: int):
        self.id = graffiti_id
        self.owner_id = owner_id
        self.url = url
        self.width = width
        self.height = height

    def to_dict(self) -> dict:
        """Returns the graffiti object as a dictionary."""
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "url": self.url,
            "width": self.width,
            "height": self.height
        }
