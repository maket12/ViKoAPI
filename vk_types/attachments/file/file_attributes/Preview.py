from vk_types.attachments.photo.Photo import Photo
from vk_types.attachments.graffiti.Graffiti import Graffiti
from vk_types.attachments.voice_message.VoiceMessage import VoiceMessage


class FilePreview:
    def __init__(self, photo: list[Photo] | None, graffiti: Graffiti | None,
                 voice_message: VoiceMessage | None):
        self.photo = photo
        self.graffiti = graffiti
        self.voice_message = voice_message

    def to_dict(self) -> dict:
        """Returns the file preview object as a dictionary."""
        return {
            "photo": {
                "sizes": [size.to_dict() for size in self.photo] if self.photo else None
            },
            "graffiti": self.graffiti.to_dict() if self.graffiti else None,
            "voice_message": self.voice_message.to_dict() if self.voice_message else None,
        }
