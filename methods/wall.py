from typing import Union, Coroutine, Any
from core.session_mixin import SessionMixin
from enums.wall.filters import WallFilters
from enums.club.fields import ClubFields
from enums.user.fields import UserFields
from errors.exceptions import *


class WallMethods(SessionMixin):
    def check_link(self, link: str) -> Coroutine[Any, Any, bool]:
        params = {"link": link}
        return self.request_async("wall.checkCopyrightLink", params)

    def close_comments(self, owner_id: int, post_id: int):
        params = {"owner_id": owner_id}

        if post_id <= 0:
            raise NegativeValueError("post_id", post_id)
        params["post_id"] = post_id

        return self.request_async("wall.closeComments", params)

    def get(self, owner_id: int = None, domain: str = None,
            offset: int = None, count: int = None,
            wall_filter: WallFilters | str = WallFilters.ALL,
            extended: bool = False,
            fields: Union[list[ClubFields], list[UserFields]] | str = None):
        params = {}
        if owner_id:
            params["owner_id"] = owner_id
        if domain:
            params["domain"] = domain
        if offset:
            params["offset"] = offset
        if count:
            params["count"] = count
        if wall_filter:
            params["filter"] = wall_filter
        if extended:
            params["extended"] = True
            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str

        return self.request_async("wall.get", params)

    def get_comment(self, owner_id: int, comment_id: int, extended: bool = False,
                    fields: Union[list[ClubFields], list[UserFields]] | str = None):
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
                     extended: bool = False, fields: Union[list[ClubFields], list[UserFields]] | str = None,
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

    def pin(self, owner_user_id: int, post_id: int):
        if post_id < 0:
            raise NegativeValueError("post_id", post_id)

        params = {
            "owner_id": owner_user_id,
            "post_id": post_id
        }
        return self.request_async("wall.pin", params)
