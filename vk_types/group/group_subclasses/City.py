class GroupCity:
    def __init__(self, city_id: int, title: str):
        self.id = city_id
        self.title = title

    def to_dict(self) -> dict:
        """Returns the group city object as a dictionary."""
        return {
            "id": self.id,
            "title": self.title
        }
