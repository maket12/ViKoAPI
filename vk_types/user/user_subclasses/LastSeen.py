from datetime import datetime
from enums.user.platform import UsersPlatform


class UsersLastSeen:
    def __init__(self, time: int, platform: UsersPlatform):
        """
        Represents user.last_seen object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param time: last seen time
        :param platform: type of platform
        """
        self.datetime = datetime.fromtimestamp(time)
        self.platform = platform

    def to_dict(self) -> dict:
        return {
            "time": int(self.datetime.timestamp()),
            "platform": self.platform.value
        }
