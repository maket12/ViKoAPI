from datetime import datetime


class GroupBanInfo:
    def __init__(self, end_unix: int, comment: str):
        self.end_datetime = datetime.fromtimestamp(end_unix)
        self.comment = comment

    def to_dict(self) -> dict:
        """Returns the group ban info object as a dictionary."""
        return {
            "end_date": self.end_datetime.isoformat(),
            "comment": self.comment
        }
