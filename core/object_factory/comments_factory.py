from core.object_factory.attachments_factory import AttachmentsFactory
from vk_types.comment.Comment import Comment
from vk_types.comment.comments_subclasses.Donut import CommentsDonut
from vk_types.comment.comments_subclasses.Thread import CommentsThread


class CommentsFactory:
    @staticmethod
    def create_comment_donut(data: dict) -> CommentsDonut:
        mapped_data = {
            "is_don": bool(data.get("is_don")),
            "placeholder": data.get("placeholder")
        }
        return CommentsDonut(**mapped_data)

    @staticmethod
    def create_comments_thread(data: dict) -> CommentsThread:
        mapped_data = {
            "count": data.get("count"),
            "items": [CommentsFactory.create_comment(comment) for comment in data.get("items")] if data.get("items") else None,
            "can_post": bool(data.get("can_post")),
            "show_reply_button": bool(data.get("count")),
            "groups_can_post": bool(data.get("groups_can_post")),
        }
        return CommentsThread(**mapped_data)

    @staticmethod
    def create_comment(data: dict) -> Comment:
        mapped_data = {
            "comment_id": data.get("id"),
            "from_id": data.get("from_id"),
            "date_in_unix": data.get("date"),
            "text": data.get("text"),
            "donut": CommentsFactory.create_comment_donut(data.get("donut")) if data.get("donut") else None,
            "reply_to_user": data.get("reply_to_user"),
            "reply_to_comment": data.get("reply_to_comment"),
            "attachments": AttachmentsFactory.create_attachments(data.get("attachments")) if data.get("attachments") else None,
            "parents_stack": data.get("parents_stack"),
            "thread": CommentsFactory.create_comments_thread(data.get("thread")) if data.get("thread") else None,
            "likes": data.get("likes").get("count") if data.get("likes") else None,
            "is_liked": bool(data.get("likes").get("is_liked")) if data.get("likes") else None,
            "can_like": bool(data.get("likes").get("can_like")) if data.get("likes") else None,
            "real_offset": data.get("real_offset"),
            "object_id": data.get("pid")
        }
        return Comment(**mapped_data)

    @staticmethod
    def create_comments(items: list) -> list[Comment]:
        return [CommentsFactory.create_comment(item) for item in items]