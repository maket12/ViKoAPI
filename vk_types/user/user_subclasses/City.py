class UsersCity:
    def __init__(self, city_id: int, title: str):
        """
        Represents user.city object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param city_id: ID of the city. Can be used to get full info about the city.
        :param title: Name of the city.
        """
        self.city_id = city_id
        self.title = title

    def to_dict(self) -> dict:
        return {
            "id": self.city_id,
            "title": self.title
        }
