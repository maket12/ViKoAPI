from core.object_factory.attachments_factory import AttachmentsFactory
from enums.group.admin_level import AdminLevel
from enums.group.type import Type
from enums.group.wall_status import WallStatus
from enums.group.age_limit import AgeLimit
from enums.group.main_section import MainSection
from enums.group.market_type import MarketType
from enums.group.member_status import MemberStatus
from vk_types.group.Group import Group
from vk_types.group.group_subclasses.BanInfo import GroupBanInfo
from vk_types.group.group_subclasses.Market import GroupMarket
from vk_types.group.group_subclasses.Link import GroupLink
from vk_types.group.group_subclasses.Cover import GroupCover
from vk_types.group.group_subclasses.City import GroupCity
from vk_types.group.group_subclasses.Counters import GroupCounters
from vk_types.group.group_subclasses.Crop import Crop
from vk_types.group.group_subclasses.CropPhoto import GroupCropPhoto
from vk_types.group.group_subclasses.Contact import GroupContact


class GroupsFactory:
    @staticmethod
    def create_group_ban_info(data: dict) -> GroupBanInfo:
        mapped_data = {
            "end_unix": data.get("end_date"),
            "comment": data.get("comment")
        }
        return GroupBanInfo(**mapped_data)

    @staticmethod
    def create_group_city(data: dict) -> GroupCity:
        mapped_data = {
            "city_id": data.get("id"),
            "title": data.get("title")
        }
        return GroupCity(**mapped_data)

    @staticmethod
    def create_group_contact(data: dict) -> GroupContact:
        mapped_data = {
            "user_id": data.get("user_id"),
            "desc": data.get("desc"),
            "phone": data.get("phone"),
            "email": data.get("email")
        }
        return GroupContact(**mapped_data)

    @staticmethod
    def create_group_contacts(items: list) -> list[GroupContact]:
        return [GroupsFactory.create_group_contact(item) for item in items]

    @staticmethod
    def create_group_counters(data: dict) -> GroupCounters:
        mapped_data = {
            "photos": data.get("photos"),
            "albums": data.get("albums"),
            "audios": data.get("audios"),
            "videos": data.get("videos"),
            "topics": data.get("topics"),
            "docs": data.get("docs")
        }
        return GroupCounters(**mapped_data)

    @staticmethod
    def create_group_cover(data: dict) -> GroupCover:
        mapped_data = {
            "is_enabled": data.get("enabled"),
            "images": AttachmentsFactory.create_photos(data.get("images")) if data.get("images") else None
        }
        return GroupCover(**mapped_data)

    @staticmethod
    def create_group_crop(data: dict) -> Crop:
        mapped_data = {
            "x": data.get("x"),
            "y": data.get("y"),
            "x2": data.get("x2"),
            "y2": data.get("y2")
        }
        return Crop(**mapped_data)

    @staticmethod
    def create_group_crop_photo(data: dict) -> GroupCropPhoto:
        mapped_data = {
            "photo": AttachmentsFactory.create_photo(data.get("photo")),
            "crop": GroupsFactory.create_group_crop(data.get("crop")),
            "rect": GroupsFactory.create_group_crop(data.get("rect")),
        }
        return GroupCropPhoto(**mapped_data)

    @staticmethod
    def create_group_link(data: dict) -> GroupLink:
        mapped_data = {
            "link_id": data.get("id"),
            "url": data.get("url"),
            "name": data.get("name"),
            "desc": data.get("desc"),
            "photo_50": data.get("photo_50"),
            "photo_100": data.get("photo_100")
        }
        return GroupLink(**mapped_data)

    @staticmethod
    def create_group_links(items: list) -> list[GroupLink]:
        return [GroupsFactory.create_group_link(item) for item in items]

    @staticmethod
    def create_group_market(data: dict) -> GroupMarket:
        mapped_data = {
            "is_enabled": bool(data.get("enabled")),
            "market_type": MarketType(data.get("type")).name,
            "price_min": data.get("price_min"),
            "price_max": data.get("price_max"),
            "main_album_id": data.get("main_album_id"),
            "contact_id": data.get("contact_id"),
            "currency": AttachmentsFactory.create_price_currency(data.get("currency")),
            "currency_text": data.get("currency_text")
        }
        return GroupMarket(**mapped_data)

    @staticmethod
    def create_group(data: dict) -> Group:
        mapped_data = {
            "group_id": data.get("id"),
            "name": data.get("name"),
            "screen_name": data.get("screen_name"),
            "is_closed": True if data.get("is_closed") == 1 else False,
            "is_private": True if data.get("is_closed") == 2 else False,
            "is_deleted": True if data.get("deactivated") == "deleted" else False,
            "is_banned": True if data.get("deactivated") == "banned" else False,
            "is_admin": True if data.get("is_admin") else False,
            "admin_level": AdminLevel(data.get("admin_level")).name if data.get("is_admin") else None,
            "is_member": True if data.get("is_member") else False,
            "is_advertiser": True if data.get("is_advertiser") else False,
            "invited_by": data.get("invited_by"),
            "group_type": Type(data.get("type")).name,
            "photo_50": data.get("photo_50"),
            "photo_100": data.get("photo_100"),
            "photo_200": data.get("photo_200"),
            "activity": data.get("activity")
        }
        if data.get("addresses"):
            mapped_data["address_enabled"] = bool(data.get("addresses").get("is_enabled"))
            mapped_data["main_address_id"] = data.get("addresses").get("main_address_id")
        else:
            mapped_data["address_enabled"] = None
            mapped_data["main_address_id"] = None

        if data.get("age_limits"):
            mapped_data["age_limits"] = AgeLimit(data.get("age_limits")).name
        else:
            mapped_data["age_limits"] = None

        if data.get("ban_info"):
            mapped_data["ban_info"] = GroupsFactory.create_group_ban_info(data.get("ban_info"))
        else:
            mapped_data["ban_info"] = None

        if data.get("can_create_topic"):
            mapped_data["can_create_topic"] = bool(data.get("can_create_topic"))
        else:
            mapped_data["can_create_topic"] = None

        if data.get("can_message"):
            mapped_data["can_message"] = bool(data.get("can_message"))
        else:
            mapped_data["can_message"] = None

        if data.get("can_post"):
            mapped_data["can_post"] = bool(data.get("can_post"))
        else:
            mapped_data["can_post"] = None

        if data.get("can_see_all_posts"):
            mapped_data["can_see_all_posts"] = bool(data.get("can_see_all_posts"))
        else:
            mapped_data["can_see_all_posts"] = None

        if data.get("can_upload_doc"):
            mapped_data["can_upload_doc"] = bool(data.get("can_upload_doc"))
        else:
            mapped_data["can_upload_doc"] = None

        if data.get("can_upload_story"):
            mapped_data["can_upload_story"] = bool(data.get("can_upload_story"))
        else:
            mapped_data["can_upload_story"] = None

        if data.get("can_upload_video"):
            mapped_data["can_upload_video"] = bool(data.get("can_upload_video"))
        else:
            mapped_data["can_upload_video"] = None

        if data.get("city"):
            mapped_data["city"] = GroupsFactory.create_group_city(data.get("city"))
        else:
            mapped_data["city"] = None

        if data.get("contacts"):
            mapped_data["contacts"] = GroupsFactory.create_group_contacts(data.get("contacts"))
        else:
            mapped_data["contacts"] = None

        if data.get("counters"):
            mapped_data["counters"] = GroupsFactory.create_group_counters(data.get("counters"))
        else:
            mapped_data["counters"] = None

        if data.get("cover"):
            mapped_data["cover"] = GroupsFactory.create_group_cover(data.get("cover"))
        else:
            mapped_data["cover"] = None

        if data.get("crop_photo"):
            mapped_data["crop_photo"] = GroupsFactory.create_group_crop_photo(data.get("crop_photo"))
        else:
            mapped_data["crop_photo"] = None

        mapped_data["description"] = data.get("description")
        mapped_data["fixed_post"] = data.get("fixed_post")

        if data.get("has_photo"):
            mapped_data["has_photo"] = bool(data.get("has_photo"))
        else:
            mapped_data["has_photo"] = None

        if data.get("is_favorite"):
            mapped_data["is_favorite"] = bool(data.get("is_favorite"))
        else:
            mapped_data["is_favorite"] = None

        if data.get("is_hidden_from_feed"):
            mapped_data["is_hidden_from_feed"] = bool(data.get("is_hidden_from_feed"))
        else:
            mapped_data["is_hidden_from_feed"] = None

        if data.get("is_messages_blocked"):
            mapped_data["is_messages_blocked"] = bool(data.get("is_messages_blocked"))
        else:
            mapped_data["is_messages_blocked"] = None

        if data.get("links"):
            mapped_data["links"] = GroupsFactory.create_group_links(data.get("links"))
        else:
            mapped_data["links"] = None

        mapped_data["main_album_id"] = data.get("main_album_id")

        if data.get("main_section"):
            mapped_data["main_section"] = MainSection(data.get("main_section")).name
        else:
            mapped_data["main_section"] = None

        if data.get("market"):
            mapped_data["market"] = GroupsFactory.create_group_market(data.get("market"))
        else:
            mapped_data["market"] = None

        if data.get("member_status"):
            mapped_data["member_status"] = MemberStatus(data.get("member_status")).name
        else:
            mapped_data["member_status"] = None

        mapped_data["members"] = data.get("members_count")

        if data.get("place"):
            mapped_data["place"] = AttachmentsFactory.create_place(data.get("place"))
        else:
            mapped_data["place"] = None

        mapped_data["public_date_label"] = data.get("public_date_label")
        mapped_data["site"] = data.get("site")
        mapped_data["start_unix"] = data.get("start_date")
        mapped_data["end_unix"] = data.get("finish_date")
        mapped_data["status"] = data.get("status")

        if data.get("trending"):
            mapped_data["is_trending"] = bool(data.get("trending"))
        else:
            mapped_data["is_trending"] = None

        if data.get("verified"):
            mapped_data["is_verified"] = bool(data.get("verified"))
        else:
            mapped_data["is_verified"] = None

        mapped_data["videos"] = data.get("videos_count")

        if data.get("wall"):
            mapped_data["wall_status"] = WallStatus(data.get("wall")).name
        else:
            mapped_data["wall_status"] = None

        mapped_data["wiki_page"] = data.get("wiki_page")

        return Group(**mapped_data)

    @staticmethod
    def create_groups(items: list) -> list[Group]:
        return [GroupsFactory.create_group(item) for item in items]
