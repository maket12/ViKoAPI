from vk_types.attachments.photo.Photo import Photo
from vk_types.attachments.poll.poll_attributes.Answers import PollsAnswers


class Poll:
    def __init__(self, poll_id: int, owner_id: int, created_unix: int, question: str,
                 votes: int, answers: PollsAnswers | None, is_anonymous: bool,
                 is_multiple: bool, picked_answer_ids: list[int], end_unix: int,
                 is_closed: bool, is_board: bool, can_edit: bool, can_vote: bool,
                 can_report: bool, can_share: bool, author_id: int, photo: Photo | None,
                 background: object, friends: list[int] | None):
        pass

    def to_dict(self) -> dict:
        """Returns the poll object as a dictionary."""
        return {
            
        }
