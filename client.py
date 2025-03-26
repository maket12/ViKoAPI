from core.base_session import BaseSession
from core.object_factory import ObjectFactory
from core.response_middleware import ResponseMiddleware
from methods.raw import RawMethod
from methods.status import StatusMethods
from methods.users import UsersMethods
from methods.wall import WallMethods
from methods.friends import FriendsMethods
from methods.groups import GroupsMethods
from methods.gifts import GiftsMethods


class ViKoClient:
    def __init__(self, api_token: str = None, proxy: str = None, api_version: str = "5.199"):
        self._session = BaseSession(api_token, proxy, api_version)
        self._session.set_middleware(ResponseMiddleware(ObjectFactory()))
        self.raw = RawMethod(self._session)
        self.wall = WallMethods(self._session)
        self.groups = GroupsMethods(self._session)
        self.status = StatusMethods(self._session)
        self.users = UsersMethods(self._session)
        self.friends = FriendsMethods(self._session)
        self.gifts = GiftsMethods(self._session)

    def __getattr__(self, name):
        if hasattr(self.methods, name):
            return getattr(self.methods, name)
        raise AttributeError(f"Method {name} not found.")


