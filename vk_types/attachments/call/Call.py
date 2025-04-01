from datetime import datetime
from enums.attachments.call.state import CallState


class Call:
    def __init__(self, duration: int, initiator_user_id: int, receiver_user_id: int,
                 state: CallState, time_unix: int, is_video: bool, participants: list[int]):
        self.duration = duration
        self.initiator_user_id = initiator_user_id
        self.receiver_user_id = receiver_user_id
        self.state = state
        self.starting_time = datetime.fromtimestamp(time_unix)
        self.is_video = is_video
        self.participants = participants

    def to_dict(self) -> dict:
        """Returns the call object as a dictionary."""
        return {
            "duration": self.duration,
            "initiator_id": self.initiator_user_id,
            "receiver_id": self.receiver_user_id,
            "state": self.state.value,
            "time": self.starting_time.isoformat(),
            "video": self.is_video,
            "participants": {
                "list": self.participants,
                "count": len(self.participants)
            }
        }
