class UsersConnection:
    def __init__(self, social_name: str, nickname: str):
        """
        Represents user.connection object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param social_name: Name of the social media
        :param nickname: Nickname in the social media
        """
        self.social_name = social_name
        self.nickname = nickname

    def to_dict(self) -> dict:
        return {
            self.social_name: self.nickname
        }
