class PostsReposts:
    def __init__(self, count: int, is_reposted: bool):
        """
        Represents an attribute Reposts of Post object

        :param count: Amount of reposts
        :param is_reposted: Did the current user repost this post
        """
        self.count = count
        self.is_reposted = is_reposted
