from enums.user.relative_type import RelativeType


class UsersRelative:
    def __init__(self, user_id: int | None, name: str, relative_type: RelativeType):
        """
        Represents user.relative object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param user_id:
        :param name:
        :param relative_type:
        """
        self.user_id = user_id
        self.name = name
        self.relative_type = relative_type

    def to_dict(self) -> dict:
        return {
            "id": self.user_id,
            "name": self.name,
            "type": self.relative_type.value
        }
