class CategorySection:
    def __init__(self, section_id: int, name: str):
        self.id = section_id
        self.name = name

    def to_dict(self) -> dict:
        """Returns the category section object as a dictionary."""
        return {
            "id": self.id,
            "name": self.name
        }
