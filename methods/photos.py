from datetime import datetime
from typing import Coroutine, Any, Tuple
from core.session_mixin import SessionMixin
from vk_types.attachments.photo.Photo import Photo
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

    def get(self):
        pass

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
