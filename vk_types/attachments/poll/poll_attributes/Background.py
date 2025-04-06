from vk_types.attachments.photo.Photo import Photo
from vk_types.attachments.poll.poll_attributes.BackgroundPoint import BackgroundPoint


class PollsBackground:
    def __init__(self, background_id: int, background_type: str, angle: int,
                 color: str, width: int, height: int, images: list[Photo] | None,
                 points: list[BackgroundPoint] | None):
        self.id = background_id
        self.type = background_type
        self.angle = angle
        self.color = color
        self.width = width
        self.height = height
        self.images = images
        self.points = points

    def to_dict(self) -> dict:
        """Returns the polls background object as a dictionary."""
        return {
            "id": self.id,
            "type": self.type,
            "angle": self.angle,
            "color": self.color,
            "width": self.width,
            "height": self.height,
            "images": [image.to_dict() for image in self.images],
            "points": [point.to_dict() for point in self.points]
        }
