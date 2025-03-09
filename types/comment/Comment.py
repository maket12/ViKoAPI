from datetime import datetime
from types.comment.comments_attributes.Donut import CommentsDonut
from types.comment.comments_attributes.Thread import CommentsThread


class Comment:
    def __init__(self, comment_id: int, from_user_id: int, date_in_unix: int, text: str,
                 donut: CommentsDonut, reply_to_user_id: int | None, reply_to_comment_id: int | None,
                 attachments: object | None, parents_stack: list[int], thread: CommentsThread):
        """
        Represents a comment.

        :param comment_id: Unique identifier of the comment.
        :param from_user_id: ID of the user(or group) who posted the comment.
        :param date_in_unix: Timestamp of when the comment was created (UNIX format).
        :param text: Text content of the comment.
        :param donut: Object containing information about the "Donut" subscription status.
        :param reply_to_user_id: ID of the user(or group) to whom this comment is a reply (if any).
        :param reply_to_comment_id: ID of the comment to which this is a reply (if any).
        :param attachments: Attachments included in the comment (if any).
        :param parents_stack: List of parent comment IDs (used for nested comment structures).
        :param thread: Object containing information about the comment thread.
        """
        self.comment_id = comment_id
        self.from_user_id = from_user_id
        self.date = datetime.fromtimestamp(date_in_unix)
        self.text = text
        self.donut = donut
        self.reply_to_user_id = reply_to_user_id
        self.reply_to_comment_id = reply_to_comment_id
        self.attachments = attachments
        self.parents_stack = parents_stack
        self.thread = thread

    def to_dict(self) -> dict:
        """Returns the comment as a dictionary."""
        return {
            "comment_id": self.comment_id,
            "from_user_id": self.from_user_id,
            "date": self.date.isoformat(),
            "text": self.text,
            "donut": self.donut.to_dict() if self.donut else None,
            "reply_to_user_id": self.reply_to_user_id,
            "reply_to_comment_id": self.reply_to_comment_id,
            "attachments": self.attachments,  # You might want to serialize attachments properly
            "parents_stack": self.parents_stack,
            "thread": self.thread.to_dict() if self.thread else None
        }

