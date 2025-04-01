from vk_types.attachments.photo.Photo import Photo
from vk_types.group.group_subclasses.Crop import Crop


class GroupCropPhoto:
    def __init__(self, photo: Photo, crop: Crop, rect: Crop):
        self.photo = photo
        self.crop = crop
        self.rect = rect

    def to_dict(self) -> dict:
        """Returns the group crop photo object as a dictionary."""
        return {
            "photo": self.photo.to_dict(),
            "crop": self.crop.to_dict(),
            "rect": self.rect.to_dict()
        }
