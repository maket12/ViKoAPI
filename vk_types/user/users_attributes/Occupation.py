from enums.user.occupation_type import OccupationType


class UsersOccupation:
    def __init__(self, occupation_type: OccupationType, place_id: int, place_name: str):
        self.occupation_type = occupation_type
        self.place_id = place_id
        self.place_name = place_name
