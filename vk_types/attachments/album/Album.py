from datetime import datetime
from vk_types.attachments.photo.Photo import Photo


class Album:
    def __init__(self, album_id: int, thumb: Photo | None, owner_id: int, title: str,
                 description: str, created_unix: int, updated_unix: int, size: int):
        self.id = album_id
        self.thumb = thumb
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.created_datetime = datetime.fromtimestamp(created_unix)
        self.updated_datetime = datetime.fromtimestamp(updated_unix)
        self.size = size

    def to_dict(self) -> dict:
        """Returns the album object as a dictionary."""
        return {
            "id": self.id,
            "thumb": self.thumb.to_dict(),
            "owner_id": self.owner_id,
            "title": self.title,
            "description": self.description,
            "created": datetime.isoformat(self.created_datetime),
            "updated": datetime.isoformat(self.updated_datetime),
            "size": self.size
        }
