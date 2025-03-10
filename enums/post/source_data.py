from enum import Enum


class SourceData(Enum):
    PROFILE_ACTIVITY = "profile_activity"
    PROFILE_PHOTO = "profile_photo"
    COMMENTS = "comments"
    LIKE = "like"
    POLL = "poll"
