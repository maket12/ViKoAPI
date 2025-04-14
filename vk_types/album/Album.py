from datetime import datetime
from vk_types.attachments.photo.Photo import Photo


class Album:
    def __init__(self, album_id: int, thumb_id: int | None, owner_id: int, title: str,
                 description: str | None, created_unix: int | None, updated_unix: int,
                 size: int, can_upload: bool, photo_sizes: list[Photo] | None):
        self.id = album_id
        self.thumb_id = thumb_id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.created_datetime = datetime.fromtimestamp(created_unix) if created_unix else None
        self.updated_datetime = datetime.fromtimestamp(updated_unix) if updated_unix else None
        self.size = size
        self.can_upload = can_upload

        self.photo_sizes = photo_sizes

    def to_dict(self) -> dict:
        """Returns the album object as a dictionary."""
        return {
            "id": self.id,
            "thumb_id": self.thumb_id,
            "owner_id": self.owner_id,
            "title": self.title,
            "description": self.description,
            "created": self.created_datetime.timestamp() if self.created_datetime else None,
            "updated": self.updated_datetime.timestamp() if self.updated_datetime else None,
            "size": self.size,
            "can_upload": int(self.can_upload),
            "photo_sizes": [raw_size.to_dict() for raw_size in self.photo_sizes] if self.photo_sizes else None
        }

