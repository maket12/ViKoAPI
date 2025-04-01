from vk_types.attachments.photo.Photo import Photo


class MarketAlbum:
    def __init__(self, market_album_id: int, owner_id: int, title: str, is_main: bool,
                 is_hidden: bool, photo: Photo | None, count: int):
        self.id = market_album_id
        self.owner_id = owner_id
        self.title = title
        self.is_main = is_main
        self.is_hidden = is_hidden
        self.photo = photo
        self.count = count

    def to_dict(self) -> dict:
        """Returns the market_item album object as a dictionary."""
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "title": self.title,
            "is_main": self.is_main,
            "is_hidden": self.is_hidden,
            "photo": self.photo.to_dict(),
            "count": self.count
        }
