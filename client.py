from core.base_session import BaseSession
from core.object_factory import ObjectFactory
from core.response_middleware import ResponseMiddleware
from methods import WallMethods, StatusMethods, UsersMethods


class ViKoClient:
    def __init__(self, api_token: str, api_version: str = "5.199"):
        self._session = BaseSession(api_token, api_version)
        self._session.set_middleware(ResponseMiddleware(ObjectFactory()))
        self.wall = WallMethods(self._session)
        self.status = StatusMethods(self._session)
        self.users = UsersMethods(self._session)

    def __getattr__(self, name):
        if hasattr(self.methods, name):
            return getattr(self.methods, name)
        raise AttributeError(f"Method {name} not found.")


