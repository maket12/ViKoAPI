from vk_types.attachments.photo.Photo import Photo


class GroupCover:
    def __init__(self, is_enabled: bool, images: list[Photo]):
        self.is_enabled = is_enabled
        self.images = images

    def to_dict(self) -> dict:
        """Returns the group contact object as a dictionary."""
        return {
            "enabled": self.is_enabled,
            "images": [image.to_dict() for image in self.images]
        }
