class PostsCopyright:
    def __init__(self, source_id: int, source_link: str, source_name: str,
                 source_type: str):
        """
        Represents an attribute of Post object - Copyright
        :param source_id: ID of source
        :param source_link: Link to source
        :param source_name: Name of source
        :param source_type: Type of source
        """
        self.source_id = source_id
        self.source_link = source_link
        self.source_name = source_name
        self.source_type = source_type

    def to_dict(self) -> dict:
        """Returns the post copyright object as a dictionary."""
        return {
            "source_id": self.source_id,
            "source_link": self.source_link,
            "source_name": self.source_name,
            "source_type": self.source_type
        }

