class CommentsThread:
    def __init__(self, count: int, items: list["Comment"], can_post: bool, show_reply_button: bool,
                 groups_can_post: bool):
        self.count = count
        self.items = items
        self.can_post = can_post
        self.show_reply_button = show_reply_button
        self.groups_can_post = groups_can_post

    def to_dict(self) -> dict:
        """Returns the Thread as a dictionary."""
        return {
            "count": self.count,
            "items": {item.to_dict() for item in self.items},
            "can_post": self.can_post,
            "show_reply_button": self.show_reply_button,
            "groups_can_post": self.groups_can_post
        }
