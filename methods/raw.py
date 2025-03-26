from typing import Coroutine, Any
from core.session_mixin import SessionMixin


class RawMethod(SessionMixin):
    def method(self, method_name: str, params: dict) -> Coroutine[Any, Any, object]:
        return self.request_async(method_name, params)
