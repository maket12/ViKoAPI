from enums.attachments.type import AttachmentType


class Attachment:
    def __init__(self, attachment_type: AttachmentType | str, owner_id: int, media_id: int):
        self.type = attachment_type
        self.owner_id = owner_id
        self.media_id = media_id

    def to_dict(self) -> dict:
        """Returns the attachment object as a dictionary."""
        return {
            "type": self.type.value if isinstance(self.type, AttachmentType) else self.type,
            "owner_id": self.owner_id,
            "media_id": self.media_id
        }
