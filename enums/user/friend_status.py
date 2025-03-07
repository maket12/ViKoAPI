from enum import IntEnum


class FriendStatus(IntEnum):
    NOT_FRIEND = 0
    OUTGOING_REQUEST = 1
    INCOMING_REQUEST = 2
    FRIEND = 3
