from datetime import datetime
from enums.post.type import PostType
from vk_types.post.post_subclasses.Comments import PostsComments
from vk_types.post.post_subclasses.Copyright import PostsCopyright
from vk_types.post.post_subclasses.Likes import PostsLikes
from vk_types.post.post_subclasses.Source import PostsSource
from vk_types.attachments.Attachment import Attachment
from vk_types.attachments.geo_place.GeoPlace import GeoPlace
from vk_types.post.post_subclasses.Donut import PostsDonut


class Post:
    def __init__(self, post_id: int, owner_user_id: int | None, from_user_id: int | None,
                 created_by_user_id: int | None, date_unix: int, text: str,
                 reply_owner_user_id: int | None, reply_post_id: int | None,
                 for_friends_only: bool, comments: PostsComments | None, copyright: PostsCopyright,
                 likes: PostsLikes | None, reposts: int | None, is_reposted: bool | None, views: int,
                 post_type: PostType, post_source: PostsSource | None, signer_user_id: int | None,
                 attachments: list[Attachment] | None, geo: GeoPlace | None, reposts_history: list['Post'] | None,
                 can_pin: bool, can_delete: bool, can_edit: bool,
                 is_pinned: bool, is_add: bool, is_favorite: bool, donut: PostsDonut | None,
                 postponed_id: int | None):
        """
        Represents the Post object

        :param post_id: Post ID
        :param owner_user_id: ID of the wall owner where the post is published
        :param from_user_id: ID of the post author
        :param created_by_user_id: ID of the admin who published the post
        :param date_unix: Publication date in Unix format
        :param text: Text of the post
        :param reply_owner_user_id: ID of the owner of the post to which this post is a reply
        :param reply_post_id: ID of the post to which this post is a reply
        :param for_friends_only: Indicates if the post is for friends only
        :param comments: Information about comments to the post
        :param copyright: Information about the source of the material
        :param likes: Information about likes to the post
        :param reposts: Amount of reposts of the post
        :param is_reposted: Information about does the current user reposted post
        :param views: Number of views of the post
        :param post_type: Type of post (PostType)
        :param post_source: Information about the method of post publication
        :param signer_user_id: ID of the author if the post is published on behalf of the community
        :param attachments: Attachments in the post (media, links)
        :param geo: Information about the location
        :param reposts_history: History of reposts for the post
        :param can_pin: Whether the post can be pinned
        :param can_delete: Whether the post can be deleted
        :param can_edit: Whether the post can be edited
        :param is_pinned: Whether the post is pinned
        :param is_add: Whether the post is added to bookmarks
        :param is_favorite: Whether the post is added to favorites
        :param donut: Info about VK Donut
        :param postponed_id: ID of the postponed post
        """
        self.post_id = post_id
        self.owner_user_id = owner_user_id
        self.from_user_id = from_user_id
        self.created_by_user_id = created_by_user_id
        self.publish_datetime = datetime.fromtimestamp(date_unix)
        self.text = text
        self.reply_owner_user_id = reply_owner_user_id
        self.reply_post_id = reply_post_id
        self.for_friends_only = for_friends_only
        self.comments = comments
        self.copyright = copyright
        self.likes = likes
        self.reposts = reposts
        self.is_reposted = is_reposted
        self.views = views
        self.post_type = post_type
        self.post_source = post_source
        self.attachments = attachments
        self.geo = geo
        self.signer_user_id = signer_user_id
        self.reposts_history = reposts_history
        self.can_pin = can_pin
        self.can_delete = can_delete
        self.can_edit = can_edit
        self.is_pinned = is_pinned
        self.is_favorite = is_favorite
        self.is_add = is_add
        self.donut = donut
        self.postponed_id = postponed_id

    def to_dict(self) -> dict:
        """Returns the post object as a dictionary."""
        return {
            "post_id": self.post_id,
            "owner_id": self.owner_user_id,
            "from_id": self.from_user_id,
            "created_by": self.created_by_user_id,
            "date": self.publish_datetime.isoformat(),
            "text": self.text,
            "reply_owner_user_id": self.reply_owner_user_id,
            "reply_post_id": self.reply_post_id,
            "for_friends_only": self.for_friends_only,
            "comments": self.comments.to_dict() if self.comments else None,
            "copyright": self.copyright.to_dict() if self.copyright else None,
            "likes": self.likes.to_dict() if self.likes else None,
            "reposts": {
                "count": self.reposts,
                "is_reposted": self.is_reposted
            },
            "views": self.views,
            "post_type": self.post_type.value if self.post_type else None,
            "post_source": self.post_source.to_dict() if self.post_source else None,
            "signer_user_id": self.signer_user_id,
            "attachments": [a.to_dict() for a in self.attachments] if self.attachments else None,
            "geo": self.geo.to_dict() if self.geo else None,
            "reposts_history": [r.to_dict() for r in self.reposts_history] if self.reposts_history else None,
            "can_pin": self.can_pin,
            "can_delete": self.can_delete,
            "can_edit": self.can_edit,
            "is_pinned": self.is_pinned,
            "is_add": self.is_add,
            "is_favorite": self.is_favorite,
            "donut": self.donut.to_dict() if self.donut else None,
            "postponed_id": self.postponed_id
        }

