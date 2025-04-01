from datetime import datetime
from vk_types.attachments.photo.Photo import Photo
from enums.user.platform import UsersPlatform
from enums.attachments.video_type import VideoType
from enums.attachments.video_live_status import VideoLiveStatus


class Video:
    def __init__(self, video_id: int, owner_id: int, title: str, description: str,
                 duration: int, image: list[Photo] | None,
                 first_frame: list[Photo] | None, created_unix: int,
                 adding_unix: int, views: int, local_views: int | None, comments: int,
                 player: str, platform: UsersPlatform | None, can_add: bool, is_private: bool,
                 is_favorite: bool, can_comment: bool, can_edit: bool, can_like: bool,
                 can_repost: bool, can_subscribe: bool, can_add_to_faves: bool,
                 can_attach_link: bool, width: int, height: int, user_id: int | None,
                 is_converting: int, is_added: bool, is_subscribed: bool, is_repeat: bool,
                 is_processing: bool, video_type: VideoType, donut_balance: int,
                 access_key: str | None, is_live: bool, is_upcoming: bool,
                 live_start_unix: int | None, live_status: VideoLiveStatus | None,
                 spectators: int, likes: int, is_liked: bool, reposts: int,
                 reposts_wall: int, reposts_mail: int, is_reposted: bool):
        self.id = video_id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.duration = duration
        self.image = image
        self.first_frame = first_frame
        self.created_datetime = datetime.fromtimestamp(created_unix)
        self.adding_datetime = datetime.fromtimestamp(adding_unix)
        self.views = views
        self.local_views = local_views
        self.comments = comments
        self.player = player
        self.platform = platform
        self.can_add = can_add
        self.is_private = is_private
        self.is_favorite = is_favorite
        self.can_comment = can_comment
        self.can_edit = can_edit
        self.can_like = can_like
        self.can_repost = can_repost
        self.can_subscribe = can_subscribe
        self.can_add_to_faves = can_add_to_faves
        self.can_attach_link = can_attach_link
        self.width = width
        self.height = height
        self.user_id = user_id
        self.is_converting = is_converting
        self.is_added = is_added
        self.is_subscribed = is_subscribed
        self.is_repeat = is_repeat
        self.is_processing = is_processing
        self.video_type = video_type
        self.donut_balance = donut_balance
        self.access_key = access_key
        self.is_live = is_live
        self.is_upcoming = is_upcoming
        self.live_start_datetime = datetime.fromtimestamp(live_start_unix) if live_start_unix else None
        self.live_status = live_status
        self.spectators = spectators
        self.likes = likes
        self.is_liked = is_liked
        self.reposts = reposts
        self.reposts_wall = reposts_wall
        self.reposts_mail = reposts_mail
        self.is_reposted = is_reposted

    def to_dict(self) -> dict:
        """Returns the video object as a dictionary."""
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "title": self.title,
            "description": self.description,
            "duration": self.duration,
            "image": [img.to_dict() for img in self.image] if self.image else None,
            "first_frame": [frame.to_dict() for frame in self.first_frame] if self.first_frame else None,
            "created_datetime": self.created_datetime.isoformat(),
            "adding_datetime": self.adding_datetime.isoformat(),
            "views": self.views,
            "local_views": self.local_views,
            "comments": self.comments,
            "player": self.player,
            "platform": self.platform.value if self.platform else None,
            "can_add": self.can_add,
            "is_private": self.is_private,
            "is_favorite": self.is_favorite,
            "can_comment": self.can_comment,
            "can_edit": self.can_edit,
            "can_like": self.can_like,
            "can_repost": self.can_repost,
            "can_subscribe": self.can_subscribe,
            "can_add_to_faves": self.can_add_to_faves,
            "can_attach_link": self.can_attach_link,
            "width": self.width,
            "height": self.height,
            "user_id": self.user_id,
            "is_converting": self.is_converting,
            "is_added": self.is_added,
            "is_subscribed": self.is_subscribed,
            "is_repeat": self.is_repeat,
            "is_processing": self.is_processing,
            "video_type": self.video_type.value,
            "donut_balance": self.donut_balance,
            "access_key": self.access_key,
            "is_live": self.is_live,
            "is_upcoming": self.is_upcoming,
            "live_start_datetime": self.live_start_datetime.isoformat() if self.live_start_datetime else None,
            "live_status": self.live_status.value if self.live_status else None,
            "spectators": self.spectators,
            "likes": self.likes,
            "is_liked": self.is_liked,
            "reposts": self.reposts,
            "reposts_wall": self.reposts_wall,
            "reposts_mail": self.reposts_mail,
            "is_reposted": self.is_reposted
        }
