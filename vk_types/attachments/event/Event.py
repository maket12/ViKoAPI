from datetime import datetime
from enums.attachments.event.event_status_member import EventStatusMember


class Event:
    def __init__(self, event_id: int, start_unix: int, member_status: EventStatusMember,
                 is_favorite: bool, address: str, text: str, button_text: str,
                 friends: list[int]):
        self.id = event_id
        self.datetime = datetime.fromtimestamp(start_unix)
        self.member_status = member_status
        self.is_favorite = is_favorite
        self.address = address
        self.text = text
        self.button_text = button_text
        self.friends = friends

    def to_dict(self) -> dict:
        """Returns the event object as a dictionary."""
        return {
            "id": self.id,
            "time": datetime.isoformat(self.datetime),
            "member_status": self.member_status.value,
            "is_favorite": self.is_favorite,
            "address": self.address,
            "text": self.text,
            "button_text": self.button_text,
            "friends": self.friends
        }
