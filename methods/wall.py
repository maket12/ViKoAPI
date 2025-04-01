from typing import Union, Coroutine, Any, Tuple
from core.session_mixin import SessionMixin
from enums.wall.filter import WallFilter
from enums.group.fields import GroupFields
from enums.user.fields import UserFields
from vk_types.attachments.Attachment import Attachment
from vk_types.group.Group import Group
from vk_types.post.Post import Post
from vk_types.user.User import User
from errors.exceptions import *


class WallMethods(SessionMixin):
    def check_link(self, link: str) -> Coroutine[Any, Any, bool]:
        params = {"link": link}
        return self.request_async("wall.checkCopyrightLink", params)

    def close_comments(self, post_id: int,
                       owner_id: int | None = None) -> Coroutine[Any, Any, bool]:
        params = {}

        if owner_id:
            params["owner_id"] = owner_id

        if post_id <= 0:
            raise InvalidPostID(post_id)
        params["post_id"] = post_id

        return self.request_async("wall.closeComments", params)

    def create_comment(self, post_id: int, owner_id: int | None = None,
                       from_group: int | None = None, reply_to_comment: int | None = None,
                       message: str | None = None, attachments: list[Attachment] | None = None,
                       sticker_id: int | None = None,
                       guid: str | None = None) -> Coroutine[Any, Any, Tuple[int, list[int]]]:
        if post_id <= 0:
            raise InvalidPostID(post_id)
        params = {"post_id": post_id}

        if owner_id:
            params["owner_id"] = owner_id

        if from_group:
            params["from_group"] = from_group

        if reply_to_comment:
            params["reply_to_comment"] = reply_to_comment

        if message:
            params["message"] = message
        elif attachments:
            for attachment in attachments:
                attachment_str = attachment.to_str()
                params["attachments"] += f",{attachment_str}" if len(params["attachments"]) != 0 else attachment_str
        elif sticker_id:
            if sticker_id <= 0:
                raise InvalidStickerID(sticker_id)
            params["sticker_id"] = sticker_id
        else:
            raise ViKoAPIError("At least one of the parameters: message, attachments, sticker_id must have value!")

        if guid:
            params["guid"] = guid

        return self.request_async("wall.createComment", params)

    def delete(self, post_id: int,
               owner_id: int | None = None) -> Coroutine[Any, Any, None]:
        if post_id <= 0:
            raise InvalidPostID(post_id)

        params = {"post_id": post_id}

        if owner_id:
            params["owner_id"] = owner_id

        return self.request_async("wall.delete", params)

    def delete_comment(self, comment_id: int,
                       owner_id: int | None = None) -> Coroutine[Any, Any, None]:
        if comment_id <= 0:
            raise InvalidCommentID(comment_id)

        params = {"comment_id": comment_id}

        if owner_id:
            params["owner_id"] = owner_id

        return self.request_async("wall.deleteComment", params)

    def get(
            self, domain: str | None = None,
            offset: int | None = None, count: int | None = None,
            wall_filter: WallFilter | str = WallFilter.ALL,
            extended: bool = False,
            fields: Union[list[GroupFields], list[UserFields]] | str | None = None
    ) -> Coroutine[Any, Any, list[Post] | Tuple[list[Post], list[User], list[Group]]]:
        params = {}

        if domain:
            params["domain"] = domain

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        if wall_filter:
            if isinstance(wall_filter, WallFilter):
                params["filter"] = wall_filter.value
            else:
                params["filter"] = wall_filter

        if extended:
            params["extended"] = True
            if fields:
                if isinstance(fields, str):
                    params["fields"] = fields
                else:
                    params["fields"] = ','.join(field.value for field in fields)

        return self.request_async("wall.get", params)

    def get_by_id(
            self, posts: list[Tuple[int, list[int]]], extended: bool = False,
            fields: list[Union[UserFields, GroupFields]] | str | None = None,
            copy_history_depth: int | None = None
    ) -> Coroutine[Any, Any, list[Post] | Tuple[list[Post], list[User], list[Group]]]:
        params = {}

        for post_obj in posts:
            post_owner_id = post_obj[0]
            for post_id in post_obj[1]:
                post_str = f"{post_owner_id}_{post_id}"
                params["posts"] += f",{post_str}" if len(params["posts"]) != 0 else post_str

        if extended:
            params["extended"] = True
            if fields:
                if isinstance(fields, str):
                    params["fields"] = fields
                else:
                    params["fields"] = ','.join(field.value for field in fields)

        if copy_history_depth:
            params["copy_history_depth"] = copy_history_depth

        return self.request_async("wall.getById", params)

    def get_comment(
            self, comment_id: int, owner_id: int | None = None, extended: bool = False,
            fields: Union[list[GroupFields], list[UserFields]] | str | None = None
    ):
        if comment_id <= 0:
            raise NegativeValueError("comment_id", comment_id)

        params = {"owner_id": owner_id, "comment_id": comment_id}

        if extended:
            params["extended"] = 1
            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str

        return self.request_async("wall.getComment", params)

    def get_comments(self, owner_id: int, post_id: int,
                     need_likes: bool = False, start_comment_id: int = None,
                     offset: int = None, count: int = 10,
                     sort: int = -1, preview_length: int = 0,
                     extended: bool = False, fields: Union[list[GroupFields], list[UserFields]] | str = None,
                     comment_id: int = None, thread_items_count: int = None):
        """
                sort = -1 - desc(from newest to oldest)
                sort = 1 - asc(from oldest to newest)
        """
        params = {"owner_id": owner_id, "post_id": post_id}

        if need_likes:
            params["need_likes"] = 1
        if start_comment_id:
            params["start_comment_id"] = start_comment_id
        if offset:
            params["offset"] = offset
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            if count > 100:
                raise InvalidCountError(count, 100)
            params["count"] = count

        if sort == 1:
            params["sort"] = "asc"
        elif sort == -1:
            params["sort"] = "desc"
        else:
            raise UndefinedParameterValue("sort", sort)

        if preview_length:
            if preview_length < 0:
                raise NegativeValueError("preview_length", preview_length)
            params["preview_length"] = preview_length
        if extended:
            params["extended"] = True

            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str
        if comment_id is not None:
            if comment_id < 0:
                raise NegativeValueError("comment_id", comment_id)
            params["comment_id"] = comment_id
        if thread_items_count:
            params["thread_items_count"] = thread_items_count

        return self.request_async("wall.getComments", params)

    def get_reposts(self, owner_id: int, post_id: int,
                    offset: int = None, count: int = None):
        params = {"owner_id": owner_id, }

        if post_id <= 0:
            raise NegativeValueError("post_id", post_id)
        params["post_id"] = post_id

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        return self.request_async("wall.getReposts", params)

    def pin(self, post_id: int, owner_id: int | None) -> Coroutine[Any, Any, None]:
        if post_id < 0:
            raise InvalidPostID(post_id)

        params = {
            "owner_id": owner_id,
            "post_id": post_id
        }
        return self.request_async("wall.pin", params)

    def unpin(self, post_id: int, owner_id: int | None) -> Coroutine[Any, Any, None]:
        if post_id <= 0:
            raise InvalidPostID(post_id)

        params = {}

        if owner_id:
            params["owner_id"] = owner_id
        params["post_id"] = post_id

        return self.request_async("wall.unpin", params)
