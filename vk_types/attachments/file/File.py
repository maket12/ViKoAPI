from datetime import datetime
from enums.attachments.file_type import FileType
from vk_types.attachments.file.file_attributes.preview import FilePreview


class File:
    def __init__(self, file_id: int, owner_id: int, title: str, size: int, extension: str,
                 url: str, unix_date: int, file_type: FileType, preview: FilePreview | None):
        self.id = file_id
        self.owner_id = owner_id
        self.title = title
        self.size = size
        self.extension = extension
        self.url = url
        self.datetime = datetime.fromtimestamp(unix_date)
        self.type = file_type
        self.preview = preview

    def to_dict(self) -> dict:
        """Returns the file preview object as a dictionary."""
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "title": self.title,
            "size": self.size,
            "ext": self.extension,
            "url": self.url,
            "date": self.datetime.isoformat(),
            "type": self.type.value,
            "preview": self.preview.to_dict() if self.preview else None
        }
