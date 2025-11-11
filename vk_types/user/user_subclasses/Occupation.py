from enums.user.occupation_type import OccupationType


class UsersOccupation:
    def __init__(self, occupation_type: OccupationType, place_id: int, place_name: str):
        """
        Represents user.occupation object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param occupation_type:
        :param place_id:
        :param place_name:
        """
        self.occupation_type = occupation_type
        self.place_id = place_id
        self.place_name = place_name

    def to_dict(self) -> dict:
        return {
            "type": self.occupation_type.value,
            "id": self.place_id,
            "name": self.place_name
        }
