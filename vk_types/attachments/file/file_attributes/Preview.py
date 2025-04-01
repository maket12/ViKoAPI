from vk_types.attachments.photo.photo_attributes.Size import PhotoSize
from vk_types.attachments.graffiti.Graffiti import Graffiti
from vk_types.attachments.voice_message.VoiceMessage import VoiceMessage


class FilePreview:
    def __init__(self, photo: list[PhotoSize] | None, graffiti: Graffiti | None,
                 audio_message: VoiceMessage | None):
        self.photo = photo
        self.graffiti = graffiti
        self.audio_message = audio_message

    def to_dict(self) -> dict:
        """Returns the file preview object as a dictionary."""
        return {
            "photo": {
                "sizes": [size.to_dict() for size in self.photo]
            },
            "graffiti": self.graffiti.to_dict(),
            "voice_message": self.audio_message.to_dict(),
        }
