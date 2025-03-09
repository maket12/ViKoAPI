class UsersMilitary:
    def __init__(self, unit: str, unit_id: int, year_from: int, year_until: int):
        self.unit = unit
        self.unit_id = unit_id
        self.year_from = year_from
        self.year_until = year_until
        self.time_service = self.count_time_service()

    def count_time_service(self):
        return self.year_until - self.year_until
