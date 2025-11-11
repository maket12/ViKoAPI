class UsersCounters:
    def __init__(self, albums: int, videos: int, audios: int, photos: int, notes: int,
                 friends: int, gifts: int, groups: int, online_friends: int,
                 mutual_friends: int, user_videos: int, user_photos: int, followers: int,
                 pages: int, subscriptions: int):
        """
        Represents user.counters object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param albums: Count of albums
        :param videos: Count of videos
        :param audios: Count of audios
        :param photos: Count of photos
        :param notes: Count of notes
        :param friends: Count of friends
        :param gifts: Count of gifts
        :param groups: Count of groups
        :param online_friends: Count of online_friends
        :param mutual_friends: Count of mutual_friends
        :param user_videos: Count of user_videos
        :param user_photos: Count of user_photos
        :param followers: Count of followers
        :param pages: Count of pages
        :param subscriptions:Count of subscriptions
        """
        self.albums = albums
        self.videos = videos
        self.audios = audios
        self.photos = photos
        self.notes = notes
        self.friends = friends
        self.gifts = gifts
        self.groups = groups
        self.online_friends = online_friends
        self.mutual_friends = mutual_friends
        self.user_videos = user_videos
        self.user_photos = user_photos
        self.followers = followers
        self.pages = pages
        self.subscriptions = subscriptions

    def to_dict(self) -> dict:
        return {
            "albums": self.albums,
            "videos": self.videos,
            "audios": self.audios,
            "photos": self.photos,
            "notes": self.notes,
            "friends": self.friends,
            "gifts": self.gifts,
            "groups": self.groups,
            "online_friends": self.online_friends,
            "mutual_friends": self.mutual_friends,
            "user_videos": self.user_videos,
            "user_photos": self.user_photos,
            "followers": self.followers,
            "pages": self.pages,
            "subscriptions": self.subscriptions
        }
