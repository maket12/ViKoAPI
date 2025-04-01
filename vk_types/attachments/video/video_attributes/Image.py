class VideoImage:
    def __init__(self, url: str, height: int, width: int, with_padding: bool):
        self.url = url
        self.height = height
        self.width = width
        self.with_padding = with_padding

    def to_dict(self) -> dict:
        """Returns the video image object as a dictionary."""
        return {
            "url": self.url,
            "height": self.height,
            "width": self.width,
            "with_padding": int(self.with_padding)
        }
