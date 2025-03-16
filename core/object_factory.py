from vk_types.user.User import User
from vk_types.chat.Chat import Chat


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
        return Chat(**data)
