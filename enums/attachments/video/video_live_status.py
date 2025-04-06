from enum import Enum


class VideoLiveStatus(Enum):
    WAITING = "waiting"
    STARTED = "started"
    FINISHED = "finished"
    FAILED = "failed"
    UPCOMING = "upcoming"
