class PostsLikes:
    def __init__(self, count: int, is_liked: bool, can_like: bool, can_repost: bool):
        """
        Represents an attribute Likes of Post object

        :param count: Amount of likes on post
        :param is_liked: Did the current user like the post
        :param can_like: Can the current user like post
        :param can_repost: Can the current user repost it
        """
        self.count = count
        self.is_liked = is_liked
        self.can_like = can_like
        self.can_repost = can_repost

    def to_dict(self) -> dict:
        """Returns the post likes object as a dictionary."""
        return {
            "count": self.count,
            "is_liked": self.is_liked,
            "can_like": self.can_like,
            "can_repost": self.can_repost
        }

