class Button:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url

    def to_dict(self) -> dict:
        """Returns the button object as a dictionary."""
        return {
            "title": self.title,
            "url": self.url
        }
