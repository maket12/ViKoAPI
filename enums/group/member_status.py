from enum import IntEnum


class MemberStatus(IntEnum):
    NOT_PARTICIPANT = 0
    PARTICIPANT = 1
    NOT_SURE = 2
    REJECTED = 3
    WAIT_ACCEPTING = 4
    INVITED = 5
