class VideoFirstFrame:
    def __init__(self, url: str, height: int, width: int):
        self.url = url
        self.height = height
        self.width = width

    def to_dict(self) -> dict:
        """Returns the video first frame object as a dictionary."""
        return {
            "url": self.url,
            "height": self.height,
            "width": self.width
        }
