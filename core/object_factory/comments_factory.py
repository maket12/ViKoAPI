from vk_types.comment.Comment import Comment
from vk_types.comment.comments_subclasses.Donut import CommentsDonut


class CommentsFactory:
    @staticmethod
    def create_comment_donut(data: dict) -> CommentsDonut:
        mapped_data = {
            "is_don": bool(data.get("is_don")),
            "placeholder": data.get("placeholder")
        }
        return CommentsDonut(**mapped_data)

    @staticmethod
    def create_comment(data: dict) -> Comment:
        mapped_data = {
            "comment_id": data.get("id"),
            "from_id": data.get("from_id"),
            "date_in_unix": data.get("date"),
            "text": data.get("text"),
            "donut": CommentsFactory.create_comment_donut(data.get("donut")),
            "reply_to_user": data.get("reply_to_user"),
            "reply_to_comment": data.get("reply_to_comment"),
            "attachments": [data.get("attachments")],}
        #     "reply_to_comment": data.get("reply_to_comment"),
        #     "reply_to_comment": data.get("reply_to_comment"),
        #     "reply_to_comment": data.get("reply_to_comment")
        # }