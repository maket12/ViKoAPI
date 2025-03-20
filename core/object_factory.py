from vk_types.user.User import User
from vk_types.chat.Chat import Chat
from vk_types.gift_item.GiftItem import GiftItem, Gift


class ObjectFactory:
    @staticmethod
    def create_user(data: dict) -> User:
        return User(**data)

    @staticmethod
    def create_chat(data: dict) -> Chat:
        mapped_data = {
            "chat_id": data.get("id"),
            "chat_type": data.get("type"),
            "title": data.get("title"),
            "admin_user_id": data.get("admin_id"),
            "users": data.get("users"),
            "push_settings": data.get("push_settings"),
            "photo_50": data.get("photo_50"),
            "photo_100": data.get("photo_100"),
            "photo_200": data.get("photo_200"),
            "photo_base": data.get("photo_base"),
            "was_left": bool(data.get("left")),
            "was_kicked": bool(data.get("kicked"))
        }
        return Chat(**mapped_data)

    @staticmethod
    def create_gift_items(items: list):
        result = []
        for item in items:
            gift_item = ObjectFactory.create_gift_item(item)
            result.append(gift_item)
        return result

    @staticmethod
    def create_gift_item(data: dict) -> GiftItem:
        mapped_data = {
            "gift_item_id": data.get("id"),
            "from_user_id": data.get("from_id"),
            "message": data.get("message"),
            "unix_date": data.get("date"),
            "gift": ObjectFactory.create_gift(data.get("gift")),
            "privacy": data.get("privacy")
        }
        return GiftItem(**mapped_data)

    @staticmethod
    def create_gift(data: dict) -> Gift:
        mapped_data = {
            "gift_id": data.get("id"),
            "thumb_256": data.get("thumb_256"),
            "thumb_96": data.get("thumb_96"),
            "thumb_48": data.get("thumb_48")
        }
        return Gift(**mapped_data)
