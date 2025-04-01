from vk_types.chat.chat_subclasses.push_settings import ChatsPustSettings


class Chat:
    def __init__(self, chat_id: int, chat_type: str, title: str, admin_user_id: int,
                 users: list[int], push_settings: ChatsPustSettings, photo_50: str | None,
                 photo_100: str | None, photo_200: str | None, photo_base: str | None,
                 was_left: bool, was_kicked: bool):
        """
        Represents an object Chat (https://dev.vk.com/ru/reference/objects/chat)

        :param chat_id: ID of the chat
        :param chat_type: Type of the chat (e.g., 'chat', 'group', 'dialog')
        :param title: Title of the chat
        :param admin_user_id: ID of the chat administrator
        :param users: List of user IDs in the chat
        :param push_settings: Push notification settings
        :param photo_50: URL of the chat's 50px photo
        :param photo_100: URL of the chat's 100px photo
        :param photo_200: URL of the chat's 200px photo
        :param photo_base: Base URL of the chat's photo
        :param was_left: Whether the current user has left the chat
        :param was_kicked: Whether the current user was kicked from the chat
        """
        self.chat_id = chat_id
        self.chat_type = chat_type
        self.title = title
        self.admin_user_id = admin_user_id
        self.users = users
        self.push_settings = push_settings
        self.photo_50 = photo_50
        self.photo_100 = photo_100
        self.photo_200 = photo_200
        self.photo_base = photo_base
        self.was_left = was_left
        self.was_kicked = was_kicked
