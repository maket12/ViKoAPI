class GroupLink:
    def __init__(self, link_id: int, url: str, name: str, desc: str, photo_50: str,
                 photo_100: str):
        self.id = link_id
        self.url = url
        self.name = name
        self.desc = desc
        self.photo_50 = photo_50
        self.photo_100 = photo_100

    def to_dict(self) -> dict:
        """Returns the group link object as a dictionary."""
        return {
            "id": self.id,
            "url": self.url,
            "name": self.name,
            "desc": self.desc,
            "photo_50": self.photo_50,
            "photo_100": self.photo_100
        }
