from enum import Enum


class UserFields(Enum):
    ID = "id"
    NAME = "name"
    SCREEN_NAME = "screen_name"
    IS_CLOSED = "is_closed"
    DEACTIVATED = "deactivated"
    IS_ADMIN = "is_admin"
    ADMIN_LEVEL = "admin_level"
    IS_MEMBER = "is_member"
    IS_ADVERTISER = "is_advertiser"
    INVITED_BY = "invited_by"
    CLUB_TYPE = "type"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"

    """
    Optional fields
    """

    ACTIVITY = "activity"
    ADDRESSES = "addresses"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_MESSAGE = "can_message"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_UPLOAD_DOC = "can_upload_doc"
    CAN_UPLOAD_STORY = "can_upload_story"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CITY = "city"
    CONTACTS = "contacts"
    COUNTERS = "counters"
    COVER = "cover"
    CROP_PHOTO = "crop_photo"
    DESCRIPTION = "description"
    FIXED_POST = "fixed_post"
    HAS_PHOTO = "has_photo"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    """
    ...
    """

