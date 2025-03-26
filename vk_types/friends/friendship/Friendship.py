from enums.friendship.status import FriendshipsStatus


class Friendship:
    def __init__(self, user_id: int, status: FriendshipsStatus, is_request_unread: bool | None):
        self.user_id = user_id
        self.status = status
        self.is_request_unread = is_request_unread
