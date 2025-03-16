from enums.user.relative_type import RelativeType


class UsersRelative:
    def __init__(self, user_id: int | None, name: str, relative_type: RelativeType):
        self.user_id = user_id
        self.name = name
        self.relative_type = relative_type
