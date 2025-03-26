class PhotoSize:
    def __init__(self, size_type: str, url: str, width: int, height: int):
        self.type = size_type
        self.url = url
        self.width = width
        self.height = height

    def to_dict(self) -> dict:
        """Returns the photo size object as a dictionary."""
        return {
            "type": self.type,
            "url": self.url,
            "width": self.width,
            "height": self.height
        }
