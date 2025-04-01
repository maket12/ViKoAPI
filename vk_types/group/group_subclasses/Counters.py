class GroupCounters:
    def __init__(self, photos: int, albums: int, audios: int, videos: int, topics: int,
                 docs: int):
        self.photos = photos
        self.albums = albums
        self.audios = audios
        self.videos = videos
        self.topics = topics
        self.docs = docs

    def to_dict(self) -> dict:
        """Returns the group contact object as a dictionary."""
        return {
            "photos": self.photos,
            "albums": self.albums,
            "audios": self.audios,
            "videos": self.videos,
            "topics": self.topics,
            "docs": self.docs
        }
