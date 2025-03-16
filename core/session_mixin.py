from core.base_session import BaseSession
from core.object_factory import ObjectFactory


class SessionMixin:
    def __init__(self, session: BaseSession):
        self._session = session
        self._object_factory = ObjectFactory()

    def request(self, method: str, params: dict):
        return self._session._sync_request(method, params)

    def request_async(self, method: str, params: dict):
        return self._session._async_request(method, params)
