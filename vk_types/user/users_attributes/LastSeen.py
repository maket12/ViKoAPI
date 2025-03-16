from datetime import datetime
from enums.user.platform import UsersPlatform


class UsersLastSeen:
    def __init__(self, time: int, platform: UsersPlatform):
        self.datetime = datetime.fromtimestamp(time)
        self.platform = platform
