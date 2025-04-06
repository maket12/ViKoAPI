from datetime import datetime
from vk_types.attachments.photo.Photo import Photo
from vk_types.attachments.poll.poll_attributes.Answer import PollsAnswer
from vk_types.attachments.poll.poll_attributes.Background import PollsBackground


class Poll:
    def __init__(self, poll_id: int, owner_id: int, created_unix: int, question: str,
                 votes: int, answers: list[PollsAnswer] | None, is_anonymous: bool,
                 is_multiple: bool, picked_answer_ids: list[int], end_unix: int,
                 is_closed: bool, is_board: bool, can_edit: bool, can_vote: bool,
                 can_report: bool, can_share: bool, author_id: int, photo: Photo | None,
                 background: PollsBackground | None, friends: list[int] | None):
        self.id = poll_id
        self.owner_id = owner_id
        self.create_datetime = datetime.fromtimestamp(created_unix)
        self.question = question
        self.votes = votes
        self.answers = answers
        self.is_anonymous = is_anonymous
        self.is_multiple = is_multiple
        self.picked_answer_ids = picked_answer_ids
        self.end_datetime = datetime.fromtimestamp(end_unix)
        self.is_closed = is_closed
        self.is_board = is_board
        self.can_edit = can_edit
        self.can_vote = can_vote
        self.can_report = can_report
        self.can_share = can_share
        self.author_id = author_id
        self.photo = photo
        self.background = background
        self.friends = friends

    def to_dict(self) -> dict:
        """Returns the poll object as a dictionary."""
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "created": self.create_datetime.isoformat(),
            "question": self.question,
            "votes": self.votes,
            "answers": [answer.to_dict() for answer in self.answers],
            "anonymous": self.is_anonymous,
            "multiple": self.is_multiple,
            "answer_ids": self.picked_answer_ids,
            "end_date": self.end_datetime.isoformat(),
            "closed": self.is_closed,
            "is_board": self.is_board,
            "can_edit": self.can_edit,
            "can_vote": self.can_vote,
            "can_report": self.can_report,
            "can_share": self.can_share,
            "author_id": self.author_id,
            "photo": self.photo.to_dict(),
            "background": self.background.to_dict(),
            "friends": self.friends,
        }
