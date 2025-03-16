class PostsComments:
    def __init__(self, count: int, can_post: bool, groups_can_post: bool, can_close: bool,
                 can_open: bool):
        """
        Represents a Post attribute - Comments

        :param count: Amount of comments
        :param can_post: Can current user write comments on post
        :param groups_can_post: Can groups write comments on post
        :param can_close: Can current user close commenting
        :param can_open: Can current user open commenting
        """
        self.count = count
        self.can_post = can_post
        self.groups_can_post = groups_can_post
        self.can_close = can_close
        self.can_open = can_open
