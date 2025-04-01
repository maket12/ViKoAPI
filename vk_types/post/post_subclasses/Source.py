from enums.post.source_type import SourceType
from enums.post.source_platform import SourcePlatform
from enums.post.source_data import SourceData


class PostsSource:
    def __init__(self, source_type: SourceType, platform: SourcePlatform | None,
                 source_data: SourceData | None, url: str):
        self.source_type = source_type
        self.platform = platform
        self.data = source_data
        self.url = url

    def to_dict(self) -> dict:
        """Returns the post source object as a dictionary."""
        return {
            "source_type": self.source_type.value,
            "platform": self.platform.value if self.platform else None,
            "data": self.data.value if self.data else None,
            "url": self.url
        }

