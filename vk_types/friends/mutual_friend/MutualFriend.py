class MutualFriend:
    def __init__(self, user_id: int, source_user_id: int | None, target_user_id: int | None):
        self.user_id = user_id
        self.source_user_id = source_user_id
        self.target_user_id = target_user_id
