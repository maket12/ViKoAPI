from core.object_factory.attachments_factory import AttachmentsFactory
from enums.post.type import PostType
from enums.post.source_type import SourceType
from enums.post.source_data import SourceData
from enums.post.source_platform import SourcePlatform
from enums.post.donut_edit_mode import DonutsEditMode
from vk_types.post.Post import (
        Post, PostsCopyright, PostsLikes,
        PostsComments, PostsSource)
from vk_types.post.post_subclasses.Donut import PostsDonut


class PostsFactory:
    @staticmethod
    def create_post_comments(data: dict) -> PostsComments:
        mapped_data = {
            "count": data.get("count"),
            "can_post": data.get("can_post"),
            "groups_can_post": data.get("groups_can_post"),
            "can_close": data.get("can_close"),
            "can_open": data.get("can_open")
        }
        return PostsComments(**mapped_data)

    @staticmethod
    def create_post_copyright(data: dict) -> PostsCopyright:
        mapped_data = {
            "source_id": data.get("id"),
            "source_link": data.get("link"),
            "source_name": data.get("name"),
            "source_type": data.get("type")
        }
        return PostsCopyright(**mapped_data)

    @staticmethod
    def create_post_likes(data: dict) -> PostsLikes:
        mapped_data = {
            "count": data.get("count"),
            "is_liked": data.get("user_likes"),
            "can_like": data.get("can_like"),
            "can_repost": data.get("can_publish")
        }
        return PostsLikes(**mapped_data)

    @staticmethod
    def create_post_source(data: dict) -> PostsSource:
        mapped_data = {
            "source_type": SourceType(data.get("type")) if data.get("type") else None,
            "platform": SourcePlatform(data.get("platform")) if data.get("platform") else None,
            "source_data": SourceData(data.get("data")) if data.get("data") else None,
            "url": data.get("url")
        }
        return PostsSource(**mapped_data)

    @staticmethod
    def create_post_donut(data: dict) -> PostsDonut:
        mapped_data = {
            "is_donut": data.get("is_donut"),
            "paid_duration": data.get("paid_duration"),
            "placeholder": data.get("placeholder"),
            "can_publish_free_copy": data.get("can_publish_free_copy"),
            "edit_mode": DonutsEditMode(data.get("edit_mode")) if data.get("edit_mode") else None
        }
        return PostsDonut(**mapped_data)

    @staticmethod
    def create_post(data: dict) -> Post:
        mapped_data = {
            "post_id": data.get("id"),
            "owner_user_id": data.get("owner_id"),
            "from_user_id": data.get("from_id"),
            "created_by_user_id": data.get("created_by"),
            "date_unix": data.get("date"),
            "text": data.get("text"),
            "reply_owner_user_id": data.get("reply_owner_id"),
            "reply_post_id": data.get("reply_post_id"),
            "for_friends_only": data.get("friends_only"),
            "comments": PostsFactory.create_post_comments(data.get("comments")) if data.get("comments") else None,
            "copyright": PostsFactory.create_post_copyright(data.get("copyright")) if data.get("copyright") else None,
            "likes": PostsFactory.create_post_likes(data.get("likes")) if data.get("likes") else None,
            "reposts": data.get("reposts").get("count") if data.get("reposts") else None,
            "is_reposted": data.get("reposts").get("user_reposted") if data.get("is_reposted") else None,
            "views": data.get("views").get("count") if data.get("views") else None,
            "post_type": PostType(data.get("post_type")) if data.get("post_type") else None,
            "post_source": PostsFactory.create_post_source(data.get("post_source")) if data.get("post_source") else None,
            "attachments": AttachmentsFactory.create_attachments(data.get("attachments")) if data.get("attachments") else None,
            "geo": AttachmentsFactory.create_geo(data.get("geo")) if data.get("geo") else None,
            "signer_user_id": data.get("signer_id"),
            "reposts_history": PostsFactory.create_posts(data.get("copy_history")) if data.get(
                "copy_history") else None,
            "can_pin": data.get("can_pin"),
            "can_delete": data.get("can_delete"),
            "can_edit": data.get("can_edit"),
            "is_pinned": data.get("is_pinned"),
            "is_favorite": data.get("is_favorite"),
            "is_add": data.get("marked_as_ads"),
            "donut": PostsFactory.create_post_donut(data.get("donut")) if data.get("donut") else None,
            "postponed_id": data.get("postponed_id")
        }
        return Post(**mapped_data)

    @staticmethod
    def create_posts(items: list) -> list[Post]:
        return [PostsFactory.create_post(item) for item in items]