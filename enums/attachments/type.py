from enum import Enum


class AttachmentType(Enum):
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "doc"
    GRAFFITI = "graffiti"
    LINK = "link"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    PHOTOS_LIST = "photos_list"
    MARKET = "market_item"
    MARKET_ALBUM = "market_album"
    STICKER = "sticker"
    PRETTY_CARDS = "pretty_cards"
    EVENT = "event"
