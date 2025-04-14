from datetime import datetime
from vk_types.comment.comments_subclasses.Donut import CommentsDonut
from vk_types.comment.comments_subclasses.Thread import CommentsThread
from vk_types.attachments.Attachment import Attachment


class Comment:
    def __init__(self, comment_id: int, from_id: int, date_in_unix: int, text: str,
                 donut: CommentsDonut | None, reply_to_user: int | None, reply_to_comment: int | None,
                 attachments: list[Attachment] | None, parents_stack: list[int], thread: CommentsThread | None,
                 likes: int | None, is_liked: bool | None, can_like: bool | None,
                 real_offset: int | None, object_id: int | None = None):
        """
        Represents a comment.

        :param comment_id: Unique identifier of the comment.
        :param from_id: ID of the user(or group) who posted the comment.
        :param date_in_unix: Timestamp of when the comment was created (UNIX format).
        :param text: Text content of the comment.
        :param donut: Object containing information about the "Donut" subscription status.
        :param reply_to_user: ID of the user(or group) to whom this comment is a reply (if any).
        :param reply_to_comment: ID of the comment to which this is a reply (if any).
        :param attachments: Attachments included in the comment (if any).
        :param parents_stack: List of parent comment IDs (used for nested comment structures).
        :param thread: Object containing information about the comment thread.
        :param is_liked: Did current user like this comment.
        :param can_like: Can current user like this comment.
        :param real_offset: Shows real offset in comments set.
        :param object_id: ID of object from the comment was given(photo, video, etc.)
        """
        self.comment_id = comment_id
        self.from_id = from_id
        self.date = datetime.fromtimestamp(date_in_unix)
        self.text = text
        self.donut = donut
        self.reply_to_user = reply_to_user
        self.reply_to_comment = reply_to_comment
        self.attachments = attachments
        self.parents_stack = parents_stack
        self.thread = thread

        self.likes = likes
        self.is_liked = is_liked
        self.can_like = can_like
        self.real_offset = real_offset
        self.object_id = object_id

    def to_dict(self) -> dict:
        """Returns the comment as a dictionary."""
        return {
            "comment_id": self.comment_id,
            "from_id": self.from_id,
            "date": self.date.isoformat(),
            "text": self.text,
            "donut": self.donut.to_dict() if self.donut else None,
            "reply_to_user": self.reply_to_user,
            "reply_to_comment": self.reply_to_comment,
            "attachments": [a.to_dict() for a in self.attachments] if self.attachments else None,
            "parents_stack": self.parents_stack,
            "thread": self.thread.to_dict() if self.thread else None,
            "likes": {
                "count": self.likes,
                "user_likes": self.is_liked,
                "can_like": self.can_like,
            },
            "real_offset": self.real_offset,
            "object_id": self.object_id
        }

