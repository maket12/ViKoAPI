class UsersCountry:
    def __init__(self, country_id: int, title: str):
        """
        Represents user.country object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param country_id: ID of the country. Can be used to get a full info about.\n
        :param title: Name of the country.
        """
        self.country_id = country_id
        self.title = title

    def to_dict(self) -> dict:
        return {
            "country_id": self.country_id,
            "title": self.title
        }
