from datetime import datetime
from enums.attachments.call.state import CallState


class Call:
    def __init__(self, duration: int, initiator_id: int, receiver_id: int,
                 state: CallState, time_unix: int, is_video: bool, participants: list[int]):
        self.duration = duration
        self.initiator_id = initiator_id
        self.receiver_id = receiver_id
        self.state = state
        self.start_datetime = datetime.fromtimestamp(time_unix)
        self.is_video = is_video
        self.participants = participants

    def to_dict(self) -> dict:
        """Returns the call object as a dictionary."""
        return {
            "duration": self.duration,
            "initiator_id": self.initiator_id,
            "receiver_id": self.receiver_id,
            "state": self.state.value,
            "time": self.start_datetime.isoformat(),
            "video": self.is_video,
            "participants": {
                "list": self.participants,
                "count": len(self.participants)
            }
        }
