class UsersMilitary:
    def __init__(self, unit: str, unit_id: int, country_id: int,
                 year_from: int, year_until: int):
        """
        Represents user.military object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param unit:
        :param unit_id:
        :param country_id:
        :param year_from:
        :param year_until:
        """
        self.unit = unit
        self.unit_id = unit_id
        self.country_id = country_id
        self.year_from = year_from
        self.year_until = year_until
        self.time_service = self.count_time_service()

    def count_time_service(self):
        return self.year_until - self.year_until

    def to_dict(self) -> dict:
        return {
            "unit": self.unit,
            "unit_id": self.unit_id,
            "country_id": self.country_id,
            "from": self.year_from,
            "until": self.year_until
        }
