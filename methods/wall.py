from datetime import datetime
from typing import Union, Coroutine, Any, Tuple
from core.session_mixin import SessionMixin
from enums.wall.filter import WallFilter
from enums.wall.report_reason import ReportReason
from enums.group.fields import GroupFields
from enums.user.fields import UserFields
from vk_types.attachments.Attachment import Attachment
from vk_types.group.Group import Group
from vk_types.post.Post import Post
from vk_types.comment.Comment import Comment
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

    def edit_post(self, post_id: int, owner_id: int | None = None, friends_only: bool = False,
                  text: str | None = None, attachments: list[Attachment] | Attachment | None = None,
                  services: str | None = None, add_sign: bool = False,
                  publish_datetime: datetime | int | None = None, latitude: str | None = None,
                  longitude: str | None = None, place_id: int | None = None,
                  mark_as_ads: bool | None = None, close_comments: bool | None = None,
                  donut_paid_duration: int | None = None) -> Coroutine[Any, Any, int]:
        if post_id <= 0:
            raise InvalidPostID(post_id)

        if not text and not attachments:
            raise ViKoAPIError("Text or attachments must be not empty to edit post.")

        params = {}

        if owner_id:
            params["owner_id"] = owner_id

        params["post_id"] = post_id
        params["friends_only"] = friends_only

        if text:
            params["message"] = text

        if attachments:
            if isinstance(attachments, Attachment):
                params["attachments"] = attachments.to_str()
            else:
                params["attachments"] = ','.join(attachment.to_str() for attachment in attachments)

        params["services"] = services
        params["signed"] = add_sign

        if publish_datetime:
            if isinstance(publish_datetime, int):
                params["publish_date"] = str(publish_datetime)
            else:
                params["publish_date"] = publish_datetime.isoformat()

        if latitude:
            params["lat"] = latitude
        if longitude:
            params["long"] = longitude
        if place_id:
            if place_id <= 0:
                raise NegativeValueError("place_id", place_id)
            params["place_id"] = place_id

        if mark_as_ads:
            params["mark_as_ads"] = mark_as_ads
        if close_comments:
            params["close_comments"] = close_comments
        if donut_paid_duration:
            params["donut_paid_duration"] = donut_paid_duration

        return self.request_async("wall.edit", params)

    def edit_comment(self, comment_id: int, owner_id: int | None = None,
                     text: str | None = None, attachments: list[Attachment] | Attachment | None = None
                     ) -> Coroutine[Any, Any, None]:
        if comment_id <= 0:
            raise InvalidCommentID(comment_id)

        if not text and not attachments:
            raise ViKoAPIError("Text or attachments must be not empty to edit comment.")

        params = {}

        if owner_id:
            params["owner_id"] = owner_id

        params["comment_id"] = comment_id

        if text:
            params["message"] = text

        if attachments:
            if isinstance(attachments, Attachment):
                params["attachments"] = attachments.to_str()
            else:
                params["attachments"] = ','.join(attachment.to_str() for attachment in attachments)

        return self.request_async("wall.editComment", params)

    def edit_ads_stealth(self) -> None:
        pass

    def get_posts(
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

    def get_post_by_id(
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
    ) -> Coroutine[Any, Any, Comment | Tuple[Comment, list[User], list[Group]]]:
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
                     sort: bool = False, preview_length: int = 0,
                     extended: bool = False, fields: Union[list[GroupFields], list[UserFields]] | str = None,
                     comment_id: int = None, thread_items_count: int = None
                     ) -> Coroutine[Any, Any, list[Comment] | Tuple[list[Comment], list[User], list[Group]]]:
        """
                sort = False - desc(from newest to oldest)
                sort = True - asc(from oldest to newest)
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

        if sort:
            params["sort"] = "asc"
        else:
            params["sort"] = "desc"

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
                    offset: int = None,
                    count: int = None) -> Coroutine[Any, Any, Tuple[list[Post], list[User], list[Group]]]:
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

    def add_post(self, post_id: int, owner_id: int | None = None, from_group: bool = False, friends_only: bool = False,
                 text: str | None = None, attachments: list[Attachment] | Attachment | None = None,
                 services: str | None = None, add_sign: bool = False,
                 publish_datetime: datetime | int | None = None, latitude: str | None = None,
                 longitude: str | None = None, place_id: int | None = None, guid: str | None = None,
                 mark_as_ads: bool | None = None, close_comments: bool | None = None,
                 link_title: str | None = None, link_photo_id: str | None = None,
                 donut_paid_duration: int | None = None, mute_notifications: bool = False,
                 copyright: str | None = None) -> Coroutine[Any, Any, int]:
        if post_id <= 0:
            raise InvalidPostID(post_id)

        if not text and not attachments:
            raise ViKoAPIError("Text or attachments must be not empty to edit post.")

        params = {}

        if owner_id:
            params["owner_id"] = owner_id

        params["post_id"] = post_id
        params["from_group"] = from_group
        params["friends_only"] = friends_only

        if text:
            params["message"] = text

        if attachments:
            if isinstance(attachments, Attachment):
                params["attachments"] = attachments.to_str()
            else:
                params["attachments"] = ','.join(attachment.to_str() for attachment in attachments)

        params["services"] = services
        params["signed"] = add_sign

        if publish_datetime:
            if isinstance(publish_datetime, int):
                params["publish_date"] = str(publish_datetime)
            else:
                params["publish_date"] = publish_datetime.isoformat()

        if latitude:
            params["lat"] = latitude
        if longitude:
            params["long"] = longitude
        if place_id:
            if place_id <= 0:
                raise NegativeValueError("place_id", place_id)
            params["place_id"] = place_id
        if guid:
            params["guid"] = guid
        if mark_as_ads:
            params["mark_as_ads"] = mark_as_ads
        if close_comments:
            params["close_comments"] = close_comments
        if link_title:
            params["link_title"] = link_title
        if link_photo_id:
            params["link_photo_id"] = link_photo_id
        if donut_paid_duration:
            params["donut_paid_duration"] = donut_paid_duration
        if copyright:
            params["copyright"] = copyright

        params["mute_notifications"] = mute_notifications

        return self.request_async("wall.post", params)

    def add_post_ads_stealth(self) -> None:
        pass

    def repost(self, attachment: Attachment, text: str | None = None,
               group_id: int | None = None, mark_as_ads: bool = False,
               mute_notifications: bool = False) -> Coroutine[Any, Any, int]:
        params = {"object": attachment.to_str()}

        if text:
            params["message"] = text
        if group_id:
            if group_id <= 0:
                raise InvalidGroupID(group_id)
        params["mark_as_ads"] = mark_as_ads
        params["mute_notifications"] = mute_notifications

        return self.request_async("wall.repost", params)

    def report_post(self, owner_id: int, post_id: int,
                    reason: ReportReason | int | None = None) -> Coroutine[Any, Any, None]:
        params = {"owner_id": owner_id, "post_id": post_id}

        if reason:
            if isinstance(reason, int):
                if 0 <= reason <= 6 or reason == 8:
                    params["reason"] = reason
                else:
                    raise UndefinedParameterValue("reason", reason)
            else:
                params["reason"] = reason.value

        return self.request_async("wall.reportPost", params)

    def report_comment(self, owner_id: int, comment_id: int,
                       reason: ReportReason | int | None = None) -> Coroutine[Any, Any, None]:
        params = {"owner_id": owner_id, "comment_id": comment_id}

        if reason:
            if isinstance(reason, int):
                if 0 <= reason <= 6 or reason == 8:
                    params["reason"] = reason
                else:
                    raise UndefinedParameterValue("reason", reason)
            else:
                params["reason"] = reason.value

        return self.request_async("wall.reportComment", params)

    def restore_post(self, post_id: int, owner_id: int | None = None) -> Coroutine[Any, Any, None]:
        if post_id <= 0:
            raise InvalidPostID(post_id)

        params = {}

        if owner_id:
            params["owner_id"] = owner_id
        params["post_id"] = post_id

        return self.request_async("wall.restore", params)

    def restore_comment(self, comment_id: int, owner_id: int | None) -> Coroutine[Any, Any, None]:
        if comment_id <= 0:
            raise InvalidCommentID(comment_id)

        params = {}

        if owner_id:
            params["owner_id"] = owner_id
        params["comment_id"] = comment_id

        return self.request_async("wall.restoreComment", params)

    def open_comments(self, owner_id: int, post_id: int) -> Coroutine[Any, Any, None]:
        if post_id <= 0:
            raise InvalidPostID(post_id)

        params = {"owner_id": owner_id, "post_id": post_id}

        return self.request_async("wall.openComments", params)

    def parse_attached_link(self) -> None: pass

    def search(self):pass
