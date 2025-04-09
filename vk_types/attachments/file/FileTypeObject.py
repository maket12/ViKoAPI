class FileTypeObject:
    def __init__(self, type_id: int, name: str, count: int):
        self.id = type_id
        self.name = name
        self.count = count

    def to_dict(self) -> dict:
        """Returns the "file type object" object as a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "count": self.count
        }
