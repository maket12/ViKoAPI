from typing import Coroutine, Any, Tuple
from core.session_mixin import SessionMixin
from enums.likes.object_type import LikesObjectType
from enums.likes.filter import LikesFilter
from errors.exceptions import *
from vk_types.user.User import User


class LikesMethods(SessionMixin):
    def like(self, object_type: LikesObjectType | str, item_id: int, owner_id: int = None,
             access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        params = {"owner_id": owner_id}

        if isinstance(object_type, LikesObjectType):
            params["type"] = object_type.value
        else:
            params["type"] = object_type

        params["item_id"] = item_id
        params["access_key"] = access_key
        params["from_group"] = from_group

        return self.request_async("likes.add", params)

    def like_post(self, post_id: int, owner_id: int = None,
                  access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.POST, post_id, owner_id, access_key, from_group)

    def like_comment(self, comment_id: int, owner_id: int = None, access_key: str = None,
                     from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.COMMENT, comment_id, owner_id, access_key, from_group)

    def like_photo(self, item_id: int, owner_id: int = None,
                   access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.POST, item_id, owner_id, access_key, from_group)

    def like_video(self, video_id: int, owner_id: int = None,
                   access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.VIDEO, video_id, owner_id, access_key, from_group)

    def like_audio(self, audio_id: int, owner_id: int = None,
                   access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.AUDIO, audio_id, owner_id, access_key, from_group)

    def like_note(self, note_id: int, owner_id: int = None,
                  access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.NOTE, note_id, owner_id, access_key, from_group)

    def like_market(self, market_id: int, owner_id: int = None,
                    access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.MARKET, market_id, owner_id, access_key, from_group)

    def like_photo_comment(self, photo_comment_id: int, owner_id: int = None,
                           access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.PHOTO_COMMENT, photo_comment_id, owner_id, access_key, from_group)

    def like_video_comment(self, video_comment_id: int, owner_id: int = None,
                           access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.VIDEO_COMMENT, video_comment_id, owner_id, access_key, from_group)

    def like_topic_comment(self, topic_comment_id: int, owner_id: int = None,
                           access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.TOPIC_COMMENT, topic_comment_id, owner_id, access_key, from_group)

    def like_market_comment(self, market_comment_id: int, owner_id: int = None,
                            access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        return self.like(LikesObjectType.MARKET_COMMENT, market_comment_id, owner_id, access_key, from_group)

    def unlike(self, object_type: LikesObjectType | str, item_id: int, owner_id: int = None,
               access_key: str = None, from_group: bool = False) -> Coroutine[Any, Any, int]:
        params = {}

        if isinstance(object_type, LikesObjectType):
            params["type"] = object_type.value
        else:
            params["type"] = object_type

        params["item_id"] = item_id
        params["owner_id"] = owner_id
        params["access_key"] = access_key
        params["from_group"] = from_group

        return self.request_async("likes.delete", params)

    def get(self, object_type: LikesObjectType | str, item_id: int, owner_id: int = None,
            page_url: str = None, likes_filter: LikesFilter | str = None,
            count: int = None, offset: int = None, friends_only: bool = False,
            extended: bool = False, skip_own: bool = False) -> Coroutine[Any, Any, list[int] | list[User]]:
        params = {}

        if isinstance(object_type, LikesObjectType):
            params["type"] = object_type.value
        else:
            params["type"] = object_type

        params["item_id"] = item_id

        if owner_id:
            params["owner_id"] = owner_id

        if page_url:
            params["page_url"] = page_url

        if likes_filter:
            if isinstance(likes_filter, LikesFilter):
                params["filter"] = likes_filter.value
            else:
                params["filter"] = likes_filter

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        params["friends_only"] = int(friends_only)
        params["extended"] = int(extended)
        params["skip_own"] = int(skip_own)

        return self.request_async("likes.getList", params)

    def check(self, object_type: LikesObjectType | str, item_id: int, user_id: int = None,
              owner_id: int = None) -> Coroutine[Any, Any, Tuple[bool, bool]]:
        params = {}

        if user_id:
            if user_id <= 0:
                raise NegativeValueError("user_id", user_id)
            params["user_id"] = user_id

        params["owner_id"] = owner_id

        if isinstance(object_type, LikesObjectType):
            params["type"] = object_type.value
        else:
            params["type"] = object_type

        params["item_id"] = item_id

        return self.request_async("likes.isLiked", params)

    def check_post(self, post_id: int, user_id: int = None,
                   owner_id: int = None) -> Coroutine[Any, Any, Tuple[bool, bool]]:
        return self.check(LikesObjectType.POST, post_id, user_id, owner_id)

    def check_comment(self, comment_id: int, user_id: int = None,
                      owner_id: int = None) -> Coroutine[Any, Any, Tuple[bool, bool]]:
        return self.check(LikesObjectType.COMMENT, comment_id, user_id, owner_id)

    def check_photo(self, photo_id: int, user_id: int = None,
                    owner_id: int = None) -> Coroutine[Any, Any, Tuple[bool, bool]]:
        return self.check(LikesObjectType.PHOTO, photo_id, user_id, owner_id)

    def check_video(self, video_id: int, user_id: int = None,
                    owner_id: int = None) -> Coroutine[Any, Any, Tuple[bool, bool]]:
        return self.check(LikesObjectType.VIDEO, video_id, user_id, owner_id)

    def check_topic(self, topic_id: int, user_id: int = None,
                    owner_id: int = None) -> Coroutine[Any, Any, Tuple[bool, bool]]:
        return self.check(LikesObjectType.POST, topic_id, user_id, owner_id)
