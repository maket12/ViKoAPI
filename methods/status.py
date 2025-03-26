from typing import Coroutine, Any
from core.session_mixin import SessionMixin
from errors.exceptions import *


class StatusMethods(SessionMixin):
    def set(self, text: str, group_id: int = None):
        params = {"text": text}
        if group_id:
            if group_id < 0:
                raise InvalidGroupID(group_id)
            params["group_id"] = group_id
        return self.request_async("status.set", params)

    def get(self, user_id: int = None, group_id: int = None) -> Coroutine[Any, Any, str]:
        if user_id:
            params = {"user_id": user_id}
        elif group_id:
            if group_id < 0:
                raise InvalidGroupID(group_id)
            params = {"group_id": group_id}
        else:
            params = {}
        return self.request_async("status.get", params)

    def get_my(self) -> Coroutine[Any, Any, str]:
        params = {}
        return self.request_async("status.get", params)
