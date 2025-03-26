from datetime import datetime
from vk_types.attachments.photo.photo_attributes.size import PhotoSize


class Photo:
    def __init__(self, photo_id: int, album_id: int, owner_id: int, user_id: int,
                 text: str, unix_date: int, sizes: list[PhotoSize],
                 width: int | None, height: int | None):
        self.id = photo_id
        self.album_id = album_id
        self.owner_id = owner_id
        self.user_id = user_id
        self.text = text
        self.datetime = datetime.fromtimestamp(unix_date)
        self.sizes = sizes
        self.width = width
        self.height = height

    def to_dict(self) -> dict:
        """Returns the photo object as a dictionary."""
        return {
            "id": self.id,
            "album_id": self.album_id,
            "owner_id": self.owner_id,
            "user_id": self.user_id,
            "text": self.text,
            "date": self.datetime.isoformat(),
            "sizes": [raw_size.to_dict() for raw_size in self.sizes],
            "width": self.width,
            "height": self.height
        }
