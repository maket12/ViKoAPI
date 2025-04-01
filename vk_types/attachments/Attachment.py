from enums.attachments.type import AttachmentType
from vk_types.attachments.photo import Photo
from vk_types.attachments.audio.Audio import Audio
from vk_types.attachments.file.File import File


class Attachment:
    def __init__(self, attachment_type: AttachmentType | str,
                 attachment_object: Photo | Video | Audio | File | None,
                 owner_id: int, media_id: int):
        self.type = attachment_type
        self.object = attachment_object
        self.owner_id = owner_id
        self.media_id = media_id

    def to_str(self) -> str:
        return f"{self.type}{self.owner_id}_{self.media_id}"

    def to_dict(self) -> dict:
        """Returns the attachment object as a dictionary."""
        return {
            "type": self.type.value if isinstance(self.type, AttachmentType) else self.type,
            "object": self.object.to_dict() if self.object else None,
            "owner_id": self.owner_id,
            "media_id": self.media_id
        }
