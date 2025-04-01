from enum import IntEnum


class WallStatus(IntEnum):
    DISABLED = 0
    OPENED = 1
    RESTRICTED = 2
    CLOSED = 3
