from enums.attachments.type import AttachmentType
from vk_types.attachments.photo import Photo
from vk_types.attachments.audio.Audio import Audio
from vk_types.attachments.file.File import File
from vk_types.attachments.video.Video import Video
from vk_types.attachments.voice_message.VoiceMessage import VoiceMessage
from vk_types.attachments.graffiti.Graffiti import Graffiti
from vk_types.attachments.link.Link import Link
from vk_types.attachments.note.Note import Note
from vk_types.attachments.poll.Poll import Poll
from vk_types.attachments.wiki_page.WikiPage import WikiPage
from vk_types.attachments.album.Album import Album
from vk_types.attachments.market_item.MarketItem import MarketItem
from vk_types.attachments.market_album.MarketAlbum import MarketAlbum
from vk_types.attachments.sticker.Sticker import Sticker
from vk_types.attachments.pretty_card.PrettyCard import PrettyCard
from vk_types.attachments.event.Event import Event
from vk_types.attachments.call.Call import Call
from vk_types.attachments.gift_item.GiftItem import GiftItem
from vk_types.post.Post import Post


class Attachment:
    def __init__(
            self, attachment_type: AttachmentType,
            attachment_object: Photo | Video | Audio | File | VoiceMessage | Graffiti |
                               Link | Note | MarketItem | Post | Call | GiftItem |
                               Poll | WikiPage | Album | list[Photo] | MarketAlbum |
                               Sticker | list[PrettyCard] | Event | None,
            owner_id: int | None, media_id: int | None):
        self.type = attachment_type
        self.object = attachment_object
        self.owner_id = owner_id
        self.media_id = media_id

    def to_str(self) -> str | None:
        if self.owner_id and self.media_id:
            return f"{self.type}{self.owner_id}_{self.media_id}"
        return None

    def to_dict(self) -> dict:
        """Returns the attachment object as a dictionary."""
        result = {
            "type": self.type.value if isinstance(self.type, AttachmentType) else self.type
        }

        if isinstance(self.object, list):
            result["object"] = [obj.to_dict() for obj in self.object]
        else:
            result["object"] = self.object.to_dict() if self.object else None

        if self.owner_id:
            result["owner_id"] = self.owner_id
        if self.media_id:
            result["media_id"] = self.media_id

        return result
