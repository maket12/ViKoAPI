from datetime import datetime
from typing import Coroutine, Any, Tuple
from core.session_mixin import SessionMixin
from enums.attachments.photo.album_privacy import AlbumPrivacy
from enums.user.fields import UserFields
from vk_types.attachments.photo.Photo import Photo
from vk_types.comment.Comment import Comment
from vk_types.user.User import User
from vk_types.group.Group import Group
from vk_types.album.Album import Album
from errors.exceptions import *


class PhotosMethods(SessionMixin):
    def confirm_tag(self, photo_id: int, tag_id: int,
                    owner_id: int | None = None) -> Coroutine[Any, Any, None]:
        if photo_id <= 0:
            raise InvalidPhotoID(photo_id)
        if tag_id <= 0:
            raise InvalidTagID(tag_id)

        params = {"photo_id": photo_id, "tag_id": tag_id}

        if owner_id:
            params["owner_id"] = owner_id

        return self.request_async("photos.confirmTag", params)

    def copy(self, owner_id: int, photo_id: int,
             access_key: str | None = None) -> Coroutine[Any, Any, int]:
        if photo_id <= 0:
            raise InvalidPhotoID(photo_id)

        params = {"owner_id": owner_id, "photo_id": photo_id}

        if access_key:
            params["access_key"] = access_key

        return self.request_async("photos.copy", params)

    # def create_album(self, title: str, group_id: int | None = None, description: str | None = None,
    # privacy: AlbumPrivacy | int = AlbumPrivacy.ALL, comment_privacy: AlbumPrivacy | int = AlbumPrivacy.ALL,
    # privacy_view: str | None = None, privacy_comment: str | None = None, admins_only: bool = False,
    # comments_disabled: bool = False):

    def delete(self, photo_id: int | list[int],
               owner_id: int | None = None) -> Coroutine[Any, Any, None]:
        params = {}

        if isinstance(photo_id, int):
            if photo_id <= 0:
                raise InvalidPhotoID(photo_id)
            params["photo_id"] = photo_id
        else:
            for pid in photo_id:
                if pid <= 0:
                    raise InvalidPhotoID(pid)
                params["photos"] += f",{pid}" if params["photos"] else pid

        if owner_id:
            params["owner_id"] = owner_id

        return self.request_async("photos.delete", params)

    def delete_album(self, album_id: int, group_id: int | None = None) -> Coroutine[Any, Any, None]:
        if album_id <= 0:
            raise InvalidAlbumID(album_id)

        params = {"album_id": album_id}

        if group_id:
            params["group_id"] = group_id

        return self.request_async("photos.deleteAlbum", params)

    def delete_comment(self, comment_id: int,
                       owner_id: int | None = None) -> Coroutine[Any, Any, bool]:
        if comment_id <= 0:
            raise InvalidCommentID(comment_id)

        params = {"comment_id": comment_id}

        if owner_id:
            params["owner_id"] = owner_id

        return self.request_async("photos.deleteComment", params)

    def get(self, owner_id: int | None = None, count: int | None = None, offset: int | None = None,
            extended: bool = False, with_photo_sizes: bool = False, no_service_albums: bool = False,
            need_hidden: bool = False, skip_hidden: bool = False) -> Coroutine[Any, Any, list[Photo]]:
        params = {}

        if owner_id:
            params["owner_id"] = owner_id
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        params["extended"] = int(extended)
        params["photo_sizes"] = int(with_photo_sizes)
        params["no_service_albums"] = int(no_service_albums)
        params["need_hidden"] = int(need_hidden)
        params["skip_hidden"] = int(skip_hidden)

        return self.request_async("photos.getAll", params)

    def get_from_album(self, album_id: int | str, owner_id: int | None = None,
                       photo_ids: list[int] | int | None = None, sort: bool = False, extended: bool = False,
                       feed_type: str | None = None, feed: datetime | int | None = None,
                       with_photo_sizes: bool = False, count: int | None = None,
                       offset: int | None = None) -> Coroutine[Any, Any, list[Photo]]:
        if isinstance(album_id, int):
            if album_id <= 0:
                raise InvalidAlbumID(album_id)
        else:
            if album_id not in ["wall", "profile", "saved"]:
                raise UndefinedParameterValue("album_id", album_id)

        params = {"album_id": album_id}

        if owner_id:
            params["owner_id"] = owner_id
        if photo_ids:
            if isinstance(photo_ids, int):
                params["photo_ids"] = photo_ids
            else:
                params["photo_ids"] = ','.join(photo_ids)

        params["rev"] = int(sort)
        params["extended"] = int(extended)

        if feed_type:
            params["feed_type"] = feed_type
        if feed:
            if isinstance(feed, datetime):
                params["feed"] = int(feed.timestamp())
            else:
                params["feed"] = feed

        params["photo_sizes"] = int(with_photo_sizes)

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        return self.request_async("photos.get", params)

    def get_albums(self, owner_id: int | None = None, album_ids: list[int] | int | None = None,
                   count: int | None = None, offset: int | None = None, need_system: bool = False,
                   need_covers: bool = False, photo_sizes: bool = False) -> Coroutine[Any, Any, list[Album]]:
        params = {}

        if owner_id:
            params["owner_id"] = owner_id
        if album_ids:
            if isinstance(album_ids, int):
                params["album_ids"] = str(album_ids)
            else:
                params["album_ids"] = ','.join(album_ids)
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        params["need_system"] = int(need_system)
        params["need_covers"] = int(need_covers)
        params["photo_sizes"] = int(photo_sizes)

        return self.request_async("photos.getAlbums", params)

    def get_comments(self, photo_id: int, owner_id: int | None = None, count: int | None = None,
                     offset: int | None = None, start_comment_id: int | None = None, skip_before_id: int | None = None,
                     skip_after_id: int | None = None, sort: bool = False, access_key: str | None = None,
                     extended: bool = False, fields: list[UserFields] | str | None = None, need_likes: bool = False
                     ) -> Coroutine[Any, Any, list[Comment] | Tuple[list[Comment], list[User], list[Group]]]:
        """
            sort = False - desc(from newest to oldest)
            sort = True - asc(from oldest to newest)
        """
        if photo_id <= 0:
            raise InvalidPhotoID(photo_id)

        params = {"photo_id": photo_id}

        if owner_id:
            params["owner_id"] = owner_id
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if start_comment_id:
            if start_comment_id < 0:
                raise NegativeValueError("start_comment_id", start_comment_id)
            params["start_comment_id"] = start_comment_id
        if skip_before_id:
            if skip_before_id < 0:
                raise NegativeValueError("skip_before_id", skip_before_id)
            params["skip_before_id"] = skip_before_id
        if skip_after_id:
            if skip_after_id < 0:
                raise NegativeValueError("skip_after_id", skip_after_id)
            params["skip_after_id"] = skip_after_id

        if not sort:
            params["sort"] = "desc"
        else:
            params["sort"] = "asc"

        if access_key:
            params["access_key"] = access_key

        params["extended"] = int(extended)
        params["need_likes"] = int(need_likes)

        if extended and fields:
            if isinstance(fields, str):
                params["fields"] = fields
            else:
                params["fields"] = ','.join(field.value for field in fields)

        return self.request_async("photos.getComments", params)

    def get_comments_from_album(self, album_id: int | None = None, owner_id: int | None = None, count: int | None = None,
                                offset: int | None = None, need_likes: bool = False):
        params = {}

        if owner_id:
            params["owner_id"] = owner_id
        if album_id:
            if album_id <= 0:
                raise InvalidAlbumID(album_id)
            params["album_id"] = album_id
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        params["need_likes"] = int(need_likes)

        return self.request_async("photos.getAllComments", params)
    
    def restore_photo(self, photo_id: int, owner_id: int | None = None) -> Coroutine[Any, Any, None]:
        if photo_id <= 0:
            raise InvalidPhotoID(photo_id)

        params = {"photo_id": photo_id}

        if owner_id:
            params["owner_id"] = owner_id

        return self.request_async("photos.restore", params)

    def restore_comment(self, comment_id: int, owner_id: int | None = None) -> Coroutine[Any, Any, None]:
        if comment_id <= 0:
            raise InvalidCommentID(comment_id)

        params = {"comment_id": comment_id}

        if owner_id:
            params["owner_id"] = owner_id

        return self.request_async("photos.restoreComment", params)

    def search(self, q: str | None = None, latitude: int | None = None, longitude: int | None = None,
               start_datetime: datetime | int | None = None, end_datetime: datetime | int | None = None,
               sort: bool = False, count: int | None = None, offset: int | None = None,
               radius: int | None = None) -> Coroutine[Any, Any, list[Photo]]:
        params = {}

        if q:
            params["q"] = q

        if latitude:
            params["lat"] = latitude
        if longitude:
            params["long"] = longitude
        if start_datetime:
            if isinstance(start_datetime, datetime):
                params["start_time"] = int(start_datetime.timestamp())
            else:
                params["start_time"] = start_datetime
        if end_datetime:
            if isinstance(end_datetime, datetime):
                params["end_time"] = int(end_datetime.timestamp())
            else:
                params["end_time"] = end_datetime

        params["sort"] = int(sort)

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if radius:
            if radius < 0:
                raise NegativeValueError("radius", radius)
            params["radius"] = radius

        return self.request_async("photos.search", params)
