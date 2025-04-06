from datetime import datetime
from enums.group.admin_level import AdminLevel
from enums.group.type import Type
from enums.group.age_limit import AgeLimit
from enums.group.main_section import MainSection
from enums.group.member_status import MemberStatus
from enums.group.wall_status import WallStatus
from vk_types.group.group_subclasses.BanInfo import GroupBanInfo
from vk_types.group.group_subclasses.City import GroupCity
from vk_types.group.group_subclasses.Contact import GroupContact
from vk_types.group.group_subclasses.Counters import GroupCounters
from vk_types.group.group_subclasses.Cover import GroupCover
from vk_types.group.group_subclasses.CropPhoto import GroupCropPhoto
from vk_types.group.group_subclasses.Link import GroupLink
from vk_types.group.group_subclasses.Market import GroupMarket
from vk_types.attachments.geo_place.geoplace_subclasses.Place import Place


class Group:
    def __init__(self, group_id: int, name: str, screen_name: str, is_closed: bool,
                 is_private: bool, is_deleted: bool, is_banned: bool, is_admin: bool,
                 admin_level: AdminLevel | None, is_member: bool, is_advertiser: bool,
                 invited_by: int, group_type: Type, photo_50: str | None, photo_100: str | None,
                 photo_200: str | None, activity: str | None, address_enabled: bool | None,
                 main_address_id: int | None, age_limits: AgeLimit | None,
                 ban_info: GroupBanInfo | None, can_create_topic: bool | None,
                 can_message: bool | None, can_post: bool | None, can_see_all_posts: bool | None,
                 can_upload_doc: bool | None, can_upload_story: bool | None,
                 can_upload_video: bool | None, city: GroupCity | None,
                 contacts: list[GroupContact] | None, counters: GroupCounters | None,
                 cover: GroupCover | None, crop_photo: GroupCropPhoto | None,
                 description: str | None, fixed_post: int | None, has_photo: bool | None,
                 is_favorite: bool | None, is_hidden_from_feed: bool | None,
                 is_messages_blocked: bool | None, links: list[GroupLink] | None,
                 main_album_id: int | None, main_section: MainSection | None,
                 market: GroupMarket | None, member_status: MemberStatus | None,
                 members: int | None, place: Place | None, public_date_label: str | None,
                 site: str | None, start_unix: int | None, end_unix: int | None,
                 status: str | None, is_trending: bool | None, is_verified: bool | None,
                 videos: int | None, wall_status: WallStatus | None, wiki_page: str | None):
        self.id = group_id
        self.name = name
        self.screen_name = screen_name
        self.is_closed = is_closed
        self.is_private = is_private
        self.is_deleted = is_deleted
        self.is_banned = is_banned
        self.is_admin = is_admin
        self.admin_level = admin_level
        self.is_member = is_member
        self.is_advertiser = is_advertiser
        self.invited_by = invited_by
        self.type = group_type
        self.photo_50 = photo_50
        self.photo_100 = photo_100
        self.photo_200 = photo_200
        self.activity = activity
        self.address_enabled = address_enabled
        self.main_address_id = main_address_id
        self.age_limit = age_limits
        self.ban_info = ban_info
        self.can_create_topic = can_create_topic
        self.can_message = can_message
        self.can_post = can_post
        self.can_see_all_posts = can_see_all_posts
        self.can_upload_doc = can_upload_doc
        self.can_upload_story = can_upload_story
        self.can_upload_video = can_upload_video
        self.city = city
        self.contacts = contacts
        self.counters = counters
        self.cover = cover
        self.crop_photo = crop_photo
        self.description = description
        self.fixed_post = fixed_post
        self.has_photo = has_photo
        self.is_favorite = is_favorite
        self.is_hidden_from_feed = is_hidden_from_feed
        self.is_messages_blocked = is_messages_blocked
        self.links = links
        self.main_album_id = main_album_id
        self.main_section = main_section
        self.market = market
        self.member_status = member_status
        self.members = members
        self.place = place
        self.public_date_label = public_date_label
        self.site = site
        self.start_datetime = datetime.fromtimestamp(start_unix)
        self.end_datetime = datetime.fromtimestamp(end_unix)
        self.status = status
        self.is_trending = is_trending
        self.is_verified = is_verified
        self.videos = videos
        self.wall_status = wall_status
        self.wiki_page = wiki_page

    def to_dict(self) -> dict:
        """Returns the group object as a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "screen_name": self.screen_name,
            "is_closed": self.is_closed,
            "is_private": self.is_private,
            "is_deleted": self.is_deleted,
            "is_banned": self.is_banned,
            "is_admin": self.is_admin,
            "admin_level": self.admin_level.name if self.admin_level else None,
            "is_member": self.is_member,
            "is_advertiser": self.is_advertiser,
            "invited_by": self.invited_by,
            "type": self.type.value,
            "photo_50": self.photo_50,
            "photo_100": self.photo_100,
            "photo_200": self.photo_200,
            "activity": self.activity,
            "address_enabled": self.address_enabled,
            "main_address_id": self.main_address_id,
            "age_limit": self.age_limit.name if self.age_limit else None,
            "ban_info": self.ban_info.to_dict() if self.ban_info else None,
            "can_create_topic": self.can_create_topic,
            "can_message": self.can_message,
            "can_post": self.can_post,
            "can_see_all_posts": self.can_see_all_posts,
            "can_upload_doc": self.can_upload_doc,
            "can_upload_story": self.can_upload_story,
            "can_upload_video": self.can_upload_video,
            "city": self.city.to_dict() if self.city else None,
            "contacts": [c.to_dict() for c in self.contacts] if self.contacts else None,
            "counters": self.counters.to_dict() if self.counters else None,
            "cover": self.cover.to_dict() if self.cover else None,
            "crop_photo": self.crop_photo.to_dict() if self.crop_photo else None,
            "description": self.description,
            "fixed_post": self.fixed_post,
            "has_photo": self.has_photo,
            "is_favorite": self.is_favorite,
            "is_hidden_from_feed": self.is_hidden_from_feed,
            "is_messages_blocked": self.is_messages_blocked,
            "links": [l.to_dict() for l in self.links] if self.links else None,
            "main_album_id": self.main_album_id,
            "main_section": self.main_section.name if self.main_section else None,
            "market": self.market.to_dict() if self.market else None,
            "member_status": self.member_status.name if self.member_status else None,
            "members": self.members,
            "place": self.place.to_dict() if self.place else None,
            "public_date_label": self.public_date_label,
            "site": self.site,
            "start_date": self.start_datetime.isoformat() if self.start_datetime else None,
            "end_date": self.end_datetime.isoformat() if self.end_datetime else None,
            "status": self.status,
            "is_trending": self.is_trending,
            "is_verified": self.is_verified,
            "videos": self.videos,
            "wall_status": self.wall_status.name if self.wall_status else None,
            "wiki_page": self.wiki_page
        }

