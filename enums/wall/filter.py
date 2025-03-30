from enum import Enum


class WallFilter(Enum):
    SUGGESTS = "suggests"
    POSTPONED = "postponed"
    OWNER = "owner"
    ALL = "all"
    OTHERS = "others"
    DONUT = "donut"
