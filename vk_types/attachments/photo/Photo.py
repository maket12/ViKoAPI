from datetime import datetime


class Photo:
    def __init__(self, photo_id: int, album_id: int | None, owner_id: int | None, user_id: int | None,
                 text: str | None, unix_date: int | None, sizes: list["Photo"] | None,
                 width: int | None, height: int | None, likes: int | None, is_liked: bool | None,
                 comments: int | None, can_comment: bool | None, tags: int | None, reposts: int | None,
                 real_offset: int | None = None):
        self.id = photo_id
        self.album_id = album_id
        self.owner_id = owner_id
        self.user_id = user_id
        self.text = text
        self.datetime = datetime.fromtimestamp(unix_date) if unix_date else None
        self.sizes = sizes
        self.width = width
        self.height = height
        self.likes = likes
        self.is_liked = is_liked
        self.comments = comments
        self.can_comment = can_comment
        self.tags = tags
        self.reposts = reposts
        self.real_offset = real_offset

    def to_dict(self) -> dict:
        """Returns the photo object as a dictionary."""
        return {
            "id": self.id,
            "album_id": self.album_id,
            "owner_id": self.owner_id,
            "user_id": self.user_id,
            "text": self.text,
            "date": self.datetime.isoformat() if self.datetime else None,
            "sizes": [raw_size.to_dict() for raw_size in self.sizes] if self.sizes else None,
            "width": self.width,
            "height": self.height,
            "likes": {
                "count": self.likes,
                "user_likes": self.is_liked
            },
            "comments": self.comments,
            "can_comment": self.can_comment,
            "tags": self.tags,
            "reposts": self.reposts,
            "real_offset": self.real_offset
        }
