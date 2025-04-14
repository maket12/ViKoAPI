from enum import IntEnum


class AlbumPrivacy(IntEnum):
    ALL = 0
    FRIENDS = 1
    FRIENDS_FRIENDS = 2
    ONLY_ME = 3
