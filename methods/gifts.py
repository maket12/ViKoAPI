from typing import Coroutine, Any
from core.session_mixin import SessionMixin
from errors.exceptions import *
from vk_types.attachments.gift_item.GiftItem import GiftItem


class GiftsMethods(SessionMixin):
    def get(self, user_id: int, count: int = None, offset: int = None) -> Coroutine[Any, Any, list[GiftItem]]:
        params = {
            "user_id": user_id
        }

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        return self.request_async("gifts.get", params)

    def get_my(self, count: int = None, offset: int = None) -> Coroutine[Any, Any, list[GiftItem]]:
        params = {}

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        return self.request_async("gifts.get", params)
