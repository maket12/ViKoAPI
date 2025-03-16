from datetime import datetime
from typing import Optional


class Discussion:
    def __init__(self, discussion_id: int, title: str, created_unix_time: int,
                 created_by_user_id: int, updated_unix_time: int, updated_by_user_id: int,
                 is_closed: bool, is_fixed: bool, amount_of_comments: int,
                 first_comment: Optional[str], last_comment: Optional[str]):
        """
        Represents a discussion topic.

        :param discussion_id: Unique identifier of the discussion.
        :param title: Title of the discussion.
        :param created_unix_time: UNIX timestamp of when the discussion was created.
        :param created_by_user_id: ID of the user who created the discussion.
        :param updated_unix_time: UNIX timestamp of the last update to the discussion.
        :param updated_by_user_id: ID of the user who last updated the discussion.
        :param is_closed: Indicates if the discussion is closed.
        :param is_fixed: Indicates if the discussion is pinned at the top.
        :param amount_of_comments: Total number of comments in the discussion.
        :param first_comment: Content of the first comment in the discussion, if available.
        :param last_comment: Content of the last comment in the discussion, if available.
        """
        self.discussion_id = discussion_id
        self.title = title
        self.created_datetime = datetime.fromtimestamp(created_unix_time)
        self.created_by_user_id = created_by_user_id
        self.updated_datetime = datetime.fromtimestamp(updated_unix_time)
        self.updated_by_user_id = updated_by_user_id
        self.is_closed = is_closed
        self.is_fixed = is_fixed
        self.amount_of_comments = amount_of_comments
        self.first_comment = first_comment
        self.last_comment = last_comment

    def to_dict(self) -> dict:
        """Returns the discussion object as a dictionary."""
        return {
            "discussion_id": self.discussion_id,
            "title": self.title,
            "created_datetime": self.created_datetime.isoformat(),
            "created_by_user_id": self.created_by_user_id,
            "updated_datetime": self.updated_datetime.isoformat(),
            "updated_by_user_id": self.updated_by_user_id,
            "is_closed": self.is_closed,
            "is_fixed": self.is_fixed,
            "amount_of_comments": self.amount_of_comments,
            "first_comment": self.first_comment,
            "last_comment": self.last_comment
        }

    def is_active(self) -> bool:
        """Returns True if the discussion is still open, False otherwise."""
        return not self.is_closed
