from enums.attachments.file.file_type import FileType
from enums.attachments.video.video_type import VideoType
from enums.attachments.video.video_live_status import VideoLiveStatus
from enums.attachments.market_item.market_item_availability import MarketItemAvailability
from enums.attachments.call.state import CallState
from enums.attachments.event.event_status_member import EventStatusMember
from vk_types.button.Button import Button
from vk_types.price.Price import Price
from vk_types.price.prices_subclasses.Currency import PricesCurrency
from vk_types.attachments.Attachment import Attachment, AttachmentObjectType
from vk_types.attachments.photo.Photo import Photo
from vk_types.attachments.video.Video import Video
from vk_types.attachments.audio.Audio import Audio
from vk_types.attachments.voice_message.VoiceMessage import VoiceMessage
from vk_types.attachments.file.File import File
from vk_types.attachments.file.file_attributes.Preview import FilePreview
from vk_types.attachments.graffiti.Graffiti import Graffiti
from vk_types.attachments.link.Link import Link
from vk_types.attachments.note.Note import Note
from vk_types.attachments.geo_place.GeoPlace import GeoPlace
from vk_types.attachments.geo_place.geoplace_subclasses.Place import Place
from vk_types.attachments.gift_item.GiftItem import GiftItem, Gift
from vk_types.attachments.sticker.Sticker import Sticker
from vk_types.attachments.call.Call import Call
from vk_types.attachments.poll.Poll import Poll, PollsBackground, PollsAnswer
from vk_types.attachments.poll.poll_attributes.BackgroundPoint import BackgroundPoint
from vk_types.attachments.wiki_page.WikiPage import WikiPage
from vk_types.attachments.album.Album import Album
from vk_types.attachments.market_item.MarketItem import MarketItem
from vk_types.attachments.market_item.market_item_attributes.RejectInfo import MarketRejectInfo
from vk_types.attachments.market_item.market_item_attributes.Section import CategorySection
from vk_types.attachments.market_item.market_item_attributes.Category import MarketItemCategory
from vk_types.attachments.market_item.market_item_attributes.Dimensions import MarketItemDimensions
from vk_types.attachments.market_album.MarketAlbum import MarketAlbum
from vk_types.attachments.pretty_card.PrettyCard import PrettyCard
from vk_types.attachments.event.Event import Event
from errors.exceptions import ViKoAPIError


class AttachmentsFactory:
    @staticmethod
    def create_place(data: dict) -> Place:
        mapped_data = {
            "place_id": data.get("id"),
            "title": data.get("title"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "created_unix": data.get("created"),
            "icon": data.get("icon"),
            "checkins": data.get("checkins"),
            "updated_unix": data.get("updated"),
            "place_type": data.get("type"),
            "city": data.get("city"),
            "address": data.get("address")
        }
        return Place(**mapped_data)

    @staticmethod
    def create_geo(data: dict) -> GeoPlace:
        mapped_data = {
            "place_type": data.get("type"),
            "coordinates": data.get("coordinates"),
            "place": AttachmentsFactory.create_place(data.get("place")) if data.get("place") else None
        }
        return GeoPlace(**mapped_data)

    @staticmethod
    def create_price_currency(data: dict) -> PricesCurrency:
        mapped_data = {
            "currency_id": data.get("id"),
            "name": data.get("name")
        }
        return PricesCurrency(**mapped_data)

    @staticmethod
    def create_price(data: dict) -> Price:
        mapped_data = {
            "amount": data.get("amount"),
            "currency": AttachmentsFactory.create_price_currency(data.get("currency")),
            "text": data.get("text")
        }
        return Price(**mapped_data)

    @staticmethod
    def create_button(data: dict) -> Button:
        mapped_data = {
            "title": data.get("title"),
            "url": data.get("action").get("url")
        }
        return Button(**mapped_data)

    @staticmethod
    def create_photo(data: dict) -> Photo:
        # if data.get("url"):
        #     url = data.get("url").split('_')
        #     print(url)
        #     owner_id, photo_id = url[0].split('-')[1], url[1]
        #     mapped_data = {
        #         "photo_id": photo_id,
        #         "album_id": None,
        #         "owner_id": owner_id,
        #         "user_id": None,
        #         "text": None,
        #         "unix_date": None,
        #         "sizes": None,
        #         "width": data.get("width"),
        #         "height": data.get("height")
        #     }
        # else:
        mapped_data = {
            "photo_id": data.get("id"),
            "album_id": data.get("album_id"),
            "owner_id": data.get("owner_id"),
            "user_id": data.get("user_id"),
            "text": data.get("text"),
            "unix_date": data.get("date"),
            "sizes": [AttachmentsFactory.create_photo(size) for size in data.get("sizes")] if data.get("sizes") else None,
            "width": data.get("width"),
            "height": data.get("height")
        }
        return Photo(**mapped_data)

    @staticmethod
    def create_video(data: dict) -> Video:
        mapped_data = {
            "video_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "title": data.get("title"),
            "description": data.get("description"),
            "duration": data.get("duration"),
            "image": [AttachmentsFactory.create_photo(image) for image in data.get("image")] if data.get("image") else None,
            "first_frame": [AttachmentsFactory.create_photo(frame) for frame in data.get("first_frame")] if data.get(
                "first_frame") else None,
            "created_unix": data.get("date"),
            "adding_unix": data.get("adding_date"),
            "views": data.get("views"),
            "local_views": data.get("local_views"),
            "comments": data.get("comments"),
            "player": data.get("player"),
            "platform": data.get("platform"),
            "can_add": bool(data.get("can_add")),
            "is_private": bool(data.get("is_private")),
            "is_favorite": data.get("is_favorite"),
            "can_comment": bool(data.get("can_comment")),
            "can_edit": bool(data.get("can_edit")),
            "can_like": bool(data.get("can_like")),
            "can_repost": bool(data.get("can_repost")),
            "can_subscribe": bool(data.get("can_subscribe")),
            "can_add_to_faves": bool(data.get("can_add_to_faves")),
            "can_attach_link": bool(data.get("can_attach_link")),
            "width": data.get("width"),
            "height": data.get("height"),
            "user_id": data.get("user_id"),
            "is_converting": data.get("converting"),
            "is_added": bool(data.get("added")),
            "is_subscribed": bool(data.get("is_subscribed")),
            "is_repeat": bool(data.get("repeat")),
            "in_processing": bool(data.get("processing")),
            "video_type": VideoType(data.get("type")).name,
            "donut_balance": data.get("balance"),
            "access_key": data.get("access_key"),
            "is_live": bool(data.get("live")),
            "is_upcoming": bool(data.get("upcoming")),
            "live_start_unix": bool(data.get("live_start_time")),
            "live_status": VideoLiveStatus(data.get("live_status")).name,
            "spectators": data.get("spectators"),
            "likes": data.get("likes").get("count"),
            "is_liked": bool(data.get("likes").get("user_likes")),
            "reposts": data.get("reposts").get("count"),
            "reposts_wall": data.get("reposts").get("wall_count"),
            "reposts_mail": data.get("reposts").get("mail_count"),
            "is_reposted": bool(data.get("reposts").get("user_reposted")),
        }
        return Video(**mapped_data)

    @staticmethod
    def create_audio(data: dict) -> Audio:
        mapped_data = {
            "audio_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "artist": data.get("artist"),
            "title": data.get("title"),
            "duration": data.get("duration"),
            "url": data.get("url"),
            "lyrics_id": data.get("lyrics_id"),
            "album_id": data.get("album_id"),
            "genre_id": data.get("genre_id"),
            "unix_date": data.get("date"),
            "no_search": bool(data.get("no_search")),
            "is_hq": bool(data.get("is_hq"))
        }
        return Audio(**mapped_data)

    @staticmethod
    def create_voice_message(data: dict) -> VoiceMessage:
        mapped_data = {
            "voice_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "duration": data.get("duration"),
            "waveform": data.get("waveform"),
            "link_ogg": data.get("link_ogg"),
            "link_mp3": data.get("link_mp3")
        }
        return VoiceMessage(**mapped_data)

    @staticmethod
    def create_file_preview(data: dict) -> FilePreview:
        mapped_data = {
            "photo": data.get("photo"),
            "graffiti": data.get("graffiti"),
            "voice_message": data.get("audio_message")
        }
        return FilePreview(**mapped_data)

    @staticmethod
    def create_file(data: dict) -> File:
        mapped_data = {
            "file_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "title": data.get("title"),
            "size": data.get("size"),
            "extension": data.get("ext"),
            "url": data.get("url"),
            "unix_date": data.get("date"),
            "file_type": FileType(data.get("type")).name,
            "preview": AttachmentsFactory.create_file_preview(data.get("preview")) if data.get("preview") else None
        }
        return File(**mapped_data)

    @staticmethod
    def create_graffiti(data: dict) -> Graffiti:
        mapped_data = {
            "graffiti_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "url": data.get("url"),
            "width": data.get("width"),
            "height": data.get("height")
        }
        return Graffiti(**mapped_data)

    @staticmethod
    def create_link(data: dict) -> Link:
        mapped_data = {
            "url": data.get("url"),
            "title": data.get("title"),
            "caption": data.get("caption"),
            "description": data.get("description"),
            "photo": AttachmentsFactory.create_photo(data.get("photo")) if data.get("photo") else None,
            "product": AttachmentsFactory.create_price(data.get("product").get("price")) if data.get("product") else None,
            "button": AttachmentsFactory.create_button(data.get("button")) if data.get("button") else None,
            "preview_page": data.get("preview_page"),
            "preview_url": data.get("preview_url")
        }
        return Link(**mapped_data)

    @staticmethod
    def create_note(data: dict) -> Note:
        mapped_data = {
            "note_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "title": data.get("title"),
            "text": data.get("text"),
            "unix_date": data.get("date"),
            "comments": data.get("comments"),
            "read_comments": data.get("read_comments"),
            "view_url": data.get("view_url"),
            "privacy_view": data.get("privacy_view"),
            "can_comment": bool(data.get("can_comment")),
            "text_wiki": data.get("text_wiki")
        }
        return Note(**mapped_data)

    @staticmethod
    def create_market_item_dimensions(data: dict) -> MarketItemDimensions:
        mapped_data = {
            "width": data.get("width"),
            "height": data.get("height"),
            "length": data.get("length")
        }
        return MarketItemDimensions(**mapped_data)

    @staticmethod
    def create_category_section(data: dict) -> CategorySection:
        mapped_data = {
            "section_id": data.get("id"),
            "name": data.get("name")
        }
        return CategorySection(**mapped_data)

    @staticmethod
    def create_market_item_category(data: dict) -> MarketItemCategory:
        mapped_data = {
            "category_id": data.get("id"),
            "name": data.get("name"),
            "section": AttachmentsFactory.create_category_section(data.get("section"))
        }
        return MarketItemCategory(**mapped_data)

    @staticmethod
    def create_market_item_reject_info(data: dict) -> MarketRejectInfo:
        mapped_data = {
            "title": data.get("title"),
            "description": data.get("description"),
            "buttons": data.get("buttons"),
            "moderation_status": data.get("moderation_status"),
            "info_link": data.get("info_link"),
            "white_to_support_link": data.get("white_to_support_link"),
        }
        return MarketRejectInfo(**mapped_data)

    @staticmethod
    def create_market_item(data: dict) -> MarketItem:
        mapped_data = {
            "item_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "title": data.get("title"),
            "description": data.get("description"),
            "price": AttachmentsFactory.create_price(data.get("price")),
            "dimensions": AttachmentsFactory.create_market_item_dimensions(data.get("dimensions")),
            "weight": data.get("weight"),
            "category": AttachmentsFactory.create_market_item_category(data.get("category")),
            "thumb_photo": data.get("thumb_photo"),
            "date_unix": data.get("date"),
            "availability": MarketItemAvailability(data.get("availability")).name,
            "is_favorite": bool(data.get("is_favorite")),
            "sku": data.get("sku"),
            "reject_info": AttachmentsFactory.create_market_item_reject_info(data.get("reject_info")),
            "photos": [AttachmentsFactory.create_photo(photo) for photo in data.get("photos")] if data.get("photos") else None,
            "can_comment": bool(data.get("can_comment")) if data.get("can_comment") else None,
            "can_repost": bool(data.get("can_repost")) if data.get("can_comment") else None,
            "likes": data.get("likes").get("count") if data.get("count") else None,
            "is_liked": bool(data.get("user_likes")) if data.get("user_likes") else None,
            "url": data.get("url"),
            "button_title": data.get("button_title")
        }
        return MarketItem(**mapped_data)

    @staticmethod
    def create_call(data: dict) -> Call:
        mapped_data = {
            "duration": data.get("duration"),
            "initiator_id": data.get("initiator_id"),
            "receiver_id": data.get("receiver_id"),
            "state": CallState(data.get("state")).name,
            "time_unix": data.get("time"),
            "is_video": bool(data.get("video")),
            "participants": data.get("participants").get("list")
        }
        return Call(**mapped_data)

    @staticmethod
    def create_sticker(data: dict) -> Sticker:
        mapped_data = {
            "sticker_id": data.get("sticker_id"),
            "product_id": data.get("product_id"),
            "is_allowed": bool(data.get("is_allowed")),
            "inner_type": data.get("inner_type"),
        }
        return Sticker(**mapped_data)

    @staticmethod
    def create_gift(data: dict) -> Gift:
        mapped_data = {
            "gift_id": data.get("id"),
            "thumb_256": data.get("thumb_256"),
            "thumb_96": data.get("thumb_96"),
            "thumb_48": data.get("thumb_48")
        }
        return Gift(**mapped_data)

    @staticmethod
    def create_gift_item(data: dict) -> GiftItem:
        mapped_data = {
            "gift_item_id": data.get("id"),
            "from_user_id": data.get("from_id"),
            "message": data.get("message"),
            "unix_date": data.get("date"),
            "gift": AttachmentsFactory.create_gift(data.get("gift")),
            "privacy": data.get("privacy")
        }
        return GiftItem(**mapped_data)

    @staticmethod
    def create_gift_items(items: list) -> list[GiftItem]:
        return [AttachmentsFactory.create_gift_item(item) for item in items]

    @staticmethod
    def create_poll_answer(data: dict) -> PollsAnswer:
        mapped_data = {
            "answer_id": data.get("id"),
            "text": data.get("text"),
            "votes": data.get("votes"),
            "rate": data.get("rate")
        }
        return PollsAnswer(**mapped_data)

    @staticmethod
    def create_poll_answers(items: list) -> list[PollsAnswer]:
        return [AttachmentsFactory.create_poll_answer(item) for item in items]

    @staticmethod
    def create_poll_background_point(data: dict) -> BackgroundPoint:
        mapped_data = {
            "position": data.get("position"),
            "color": data.get("color")
        }
        return BackgroundPoint(**mapped_data)

    @staticmethod
    def create_poll_background_points(items: list) -> list[BackgroundPoint]:
        return [AttachmentsFactory.create_poll_background_point(item) for item in items]

    @staticmethod
    def create_poll_background(data: dict) -> PollsBackground:
        mapped_data = {
            "background_id": data.get("id"),
            "background_type": data.get("type"),
            "angle": data.get("angle"),
            "color": data.get("color"),
            "width": data.get("width"),
            "height": data.get("height"),
            "images": [AttachmentsFactory.create_photo(image) for image in data.get("images")] if data.get("images") else None,
            "points": AttachmentsFactory.create_poll_background_points(data.get("points")) if data.get("points") else None
        }
        return PollsBackground(**mapped_data)

    @staticmethod
    def create_poll(data: dict) -> Poll:
        mapped_data = {
            "poll_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "created_unix": data.get("created"),
            "question": data.get("question"),
            "votes": data.get("votes"),
            "answers": AttachmentsFactory.create_poll_answers(data.get("answers")) if data.get("answers") else None,
            "is_anonymous": bool(data.get("anonymous")),
            "is_multiple": bool(data.get("multiple")),
            "picked_answer_ids": data.get("answer_ids"),
            "end_unix": data.get("end_date"),
            "is_closed": bool(data.get("closed")),
            "is_board": bool(data.get("is_board")),
            "can_edit": bool(data.get("can_edit")),
            "can_vote": bool(data.get("can_vote")),
            "can_report": bool(data.get("can_report")),
            "can_share": bool(data.get("can_share")),
            "author_id": data.get("author_id"),
            "photo": AttachmentsFactory.create_photo(data.get("photo")) if data.get("photo") else None,
            "background": AttachmentsFactory.create_poll_background(data.get("background")) if data.get("background") else None,
            "friends": data.get("friends")
        }
        return Poll(**mapped_data)

    @staticmethod
    def create_wiki_page(data: dict) -> WikiPage:
        mapped_data = {
            "page_id": data.get("id"),
            "group_id": data.get("group_id"),
            "creator_id": data.get("creator_id"),
            "title": data.get("title"),
            "can_edit": bool(data.get("current_user_can_edit")),
            "can_edit_access": bool(data.get("current_user_can_edit_access")),
            "who_can_view": data.get("who_can_view"),
            "who_can_edit": data.get("who_can_edit"),
            "created_unix": data.get("created"),
            "edited_unix": data.get("edited"),
            "editor_id": data.get("editor_id"),
            "views": data.get("views"),
            "parent": data.get("parent"),
            "parent2": data.get("parent2"),
            "source": data.get("source"),
            "html": data.get("html"),
            "view_url": data.get("view_url"),
        }
        return WikiPage(**mapped_data)

    @staticmethod
    def create_album(data: dict) -> Album:
        mapped_data = {
            "album_id": data.get("id"),
            "thumb": AttachmentsFactory.create_photo(data.get("thumb")) if data.get("thumb") else None,
            "owner_id": data.get("owner_id"),
            "title": data.get("title"),
            "description": data.get("description"),
            "created_unix": data.get("created"),
            "updated_unix": data.get("updated"),
            "size": data.get("size"),
        }
        return Album(**mapped_data)

    @staticmethod
    def create_market_album(data: dict) -> MarketAlbum:
        mapped_data = {
            "market_album_id": data.get("id"),
            "owner_id": data.get("owner_id"),
            "title": data.get("title"),
            "is_main": bool(data.get("is_main")),
            "is_hidden": bool(data.get("is_hidden")),
            "photo": AttachmentsFactory.create_photo(data.get("photo")) if data.get("photo") else None,
            "count": data.get("count"),
        }
        return MarketAlbum(**mapped_data)

    @staticmethod
    def create_pretty_card(data: dict) -> PrettyCard:
        mapped_data = {
            "card_id": data.get("id"),
            "link_url": data.get("link_url"),
            "title": data.get("title"),
            "photos": [AttachmentsFactory.create_photo(image) for image in data.get("images")] if data.get("images") else None,
            "button": AttachmentsFactory.create_button(data.get("button")) if data.get("button") else None,
            "price": data.get("price"),
            "old_price": data.get("price_old")
        }
        return PrettyCard(**mapped_data)

    @staticmethod
    def create_pretty_cards(items: list) -> list[PrettyCard]:
        return [AttachmentsFactory.create_pretty_card(item) for item in items]

    @staticmethod
    def create_event(data: dict) -> Event:
        mapped_data = {
            "event_id": data.get("id"),
            "start_unix": data.get("time"),
            "member_status": EventStatusMember(data.get("member_status")).name,
            "is_favorite": bool(data.get("is_favorite")),
            "address": data.get("address"),
            "text": data.get("text"),
            "button_text": data.get("button_text"),
            "friends": data.get("friends"),
        }
        return Event(**mapped_data)

    @staticmethod
    def create_attachment(data: dict) -> Attachment:
        mapped_data = {
            "attachment_type": data.get("type")
        }

        attachment_object: AttachmentObjectType

        if data.get("photo"):
            attachment_object = AttachmentsFactory.create_photo(data.get("photo"))
        elif data.get("posted_photo"):
            attachment_object = AttachmentsFactory.create_photo(data.get("posted_photo"))
        elif data.get("video"):
            attachment_object = AttachmentsFactory.create_video(data.get("video"))
        elif data.get("audio"):
            attachment_object = AttachmentsFactory.create_audio(data.get("audio"))
        elif data.get("doc"):
            attachment_object = AttachmentsFactory.create_file(data.get("doc"))
        elif data.get("graffiti"):
            attachment_object = AttachmentsFactory.create_graffiti(data.get("graffiti"))
        elif data.get("link"):
            attachment_object = AttachmentsFactory.create_link(data.get("link"))
        elif data.get("note"):
            attachment_object = AttachmentsFactory.create_note(data.get("note"))
        elif data.get("poll"):
            attachment_object = AttachmentsFactory.create_poll(data.get("poll"))
        elif data.get("page"):
            attachment_object = AttachmentsFactory.create_wiki_page(data.get("page"))
        elif data.get("album"):
            attachment_object = AttachmentsFactory.create_album(data.get("album"))
        elif data.get("photos_list"):
            attachment_object = [AttachmentsFactory.create_photo(item) for item in data.get("photos_list").get("items")]
        elif data.get("market"):
            attachment_object = AttachmentsFactory.create_market_item(data.get("market"))
        elif data.get("market_album"):
            attachment_object = AttachmentsFactory.create_market_album(data.get("market_album"))
        elif data.get("sticker"):
            attachment_object = AttachmentsFactory.create_sticker(data.get("sticker"))
        elif data.get("pretty_cards"):
            attachment_object = AttachmentsFactory.create_pretty_cards(data.get("pretty_cards"))
        elif data.get("event"):
            attachment_object = AttachmentsFactory.create_event(data.get("event"))
        else:
            raise ViKoAPIError("Unknowing object type! Please, use the latest supported by ViKo framework version of VK API.")

        mapped_data["attachment_object"] = attachment_object

        if data.get("url"):
            url = data.get("url").split('_')
            owner_id, object_id = url[0].split('-')[1], url[1]

            mapped_data["owner_id"] = owner_id
            mapped_data["media_id"] = object_id
        else:
            mapped_data["owner_id"] = None
            mapped_data["media_id"] = None

        return Attachment(**mapped_data)

    @staticmethod
    def create_attachments(items: list) -> list[Attachment]:
        return [AttachmentsFactory.create_attachment(item) for item in items]
