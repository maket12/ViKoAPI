from datetime import datetime


class Note:
    def __init__(self, note_id: int, owner_user_id: int, title: str, text: str,
                 unix_date: int, amount_of_comments: int, amount_of_read_comments: int | None,
                 view_url: str, privacy_view: str, can_comment: bool, text_wiki: str):
        """
        Represents a note.

        :param note_id: Unique identifier of the note.
        :param owner_user_id: ID of the user who owns the note.
        :param title: Title of the note.
        :param text: Text content of the note.
        :param unix_date: Timestamp of when the note was created (UNIX format).
        :param amount_of_comments: Number of comments on the note.
        :param amount_of_read_comments: Number of read comments on the note (if available).
        :param view_url: URL for viewing the note.
        :param privacy_view: Privacy settings for viewing the note.
        :param can_comment: Indicates whether the note can be commented on.
        :param text_wiki: Text content of the note in wiki format.
        """
        self.note_id = note_id
        self.owner_user_id = owner_user_id
        self.title = title
        self.text = text
        self.note_datetime = datetime.fromtimestamp(unix_date)
        self.amount_of_comments = amount_of_comments
        self.amount_of_read_comments = amount_of_read_comments
        self.view_url = view_url
        self.privacy_view = privacy_view
        self.can_comment = can_comment
        self.text_wiki = text_wiki

    def to_dict(self) -> dict:
        """Returns the Note object as a dictionary."""
        return {
            "note_id": self.note_id,
            "owner_user_id": self.owner_user_id,
            "title": self.title,
            "text": self.text,
            "note_datetime": self.note_datetime.isoformat(),
            "amount_of_comments": self.amount_of_comments,
            "amount_of_read_comments": self.amount_of_read_comments,
            "view_url": self.view_url,
            "privacy_view": self.privacy_view,
            "can_comment": self.can_comment,
            "text_wiki": self.text_wiki
        }
