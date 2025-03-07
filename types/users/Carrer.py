class UsersCareer:
    def __init__(self, group_id: int, company: str, city_id: int, city_name: str,
                 work_from: int, work_until: int, position: str):
        self.group_id = group_id
        self.company = company
        self.city_id = city_id
        self.city_name = city_name
        self.work_from = work_from
        self.work_until = work_until
        self.position = position
