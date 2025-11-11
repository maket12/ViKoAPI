class UsersCareer:
    def __init__(self, group_id: int, company: str, country_id: int, city_id: int,
                 city_name: str, work_from: int, work_until: int, position: str):
        """
        Represents user.career object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param group_id: ID of the group if available
        :param company: Name of the company if available
        :param country_id: ID of the country
        :param city_id: ID of the city
        :param city_name: Name of the city if available
        :param work_from: Year of the beginning
        :param work_until: Year of the end
        :param position: Position
        """
        self.group_id = group_id
        self.company = company
        self.country_id = country_id
        self.city_id = city_id
        self.city_name = city_name
        self.work_from = work_from
        self.work_until = work_until
        self.position = position

    def to_dict(self) -> dict:
        return {
            "group_id": self.group_id,
            "company": self.company,
            "country_id": self.country_id,
            "city_id": self.city_id,
            "city_name": self.city_name,
            "from": self.work_from,
            "until": self.work_until,
            "position": self.position
        }
