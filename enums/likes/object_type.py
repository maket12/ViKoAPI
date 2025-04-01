from enum import Enum


class LikesObjectType(Enum):
    POST = "post"
    COMMENT = "comment"
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    NOTE = "note"
    MARKET = "market_item"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    TOPIC_COMMENT = "topic_comment"
    MARKET_COMMENT = "market_comment"
