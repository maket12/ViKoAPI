from datetime import datetime


class Audio:
    def __init__(self, audio_id: int, owner_id: int, artist: str, title: str,
                 duration: int, url: str, lyrics_id: int | None, album_id: int | None,
                 genre_id: int, unix_date: int, no_search: bool, is_hq: bool):
        self.id = audio_id
        self.owner_id = owner_id
        self.artist = artist
        self.title = title
        self.duration = duration
        self.url = url
        self.lyrics_id = lyrics_id
        self.album_id = album_id
        self.genre_id = genre_id
        self.datetime = datetime.fromtimestamp(unix_date)
        self.no_search = no_search
        self.is_hq = is_hq

    def to_dict(self) -> dict:
        """Returns the audio object as a dictionary."""
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "artist": self.artist,
            "title": self.title,
            "duration": self.duration,
            "url": self.url,
            "lyrics_id": self.lyrics_id,
            "album_id": self.album_id,
            "genre_id": self.genre_id,
            "date": self.datetime.isoformat(),
            "no_search": self.no_search,
            "is_hq": self.is_hq
        }
