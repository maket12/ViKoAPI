from typing import Coroutine, Any
from core.session_mixin import SessionMixin
from enums.user.fields import UserFields
from enums.friends.order import FriendsOrder
from errors.exceptions import *
from vk_types.friends.friendship.Friendship import Friendship
from vk_types.friends.friend_list.FriendList import FriendList
from vk_types.friends.mutual_friend.MutualFriend import MutualFriend
from vk_types.user.User import User


class FriendsMethods(SessionMixin):
    def add(self, user_id: int, text: str | None, stay_as_follower: bool) -> Coroutine[Any, Any, int]:
        params = {}

        if user_id <= 0:
            raise InvalidUserID(user_id)
        params["user_id"] = user_id

        if text:
            if len(text) > 500:
                raise TooLongText(len(text))
            params["text"] = text
        if stay_as_follower:
            params["follow"] = stay_as_follower

        return self.request_async("friends.add", params)

    def add_list(self, name: str, user_ids: list[int] = None) -> Coroutine[Any, Any, int]:
        params = {
            "name": name
        }
        if user_ids:
            for user_id in user_ids:
                if user_id <= 0:
                    raise InvalidUserID(user_id)
                params["user_ids"] += f",{user_id}" if len(params["user_ids"]) != 0 else user_id
        return self.request_async("friends.addList", params)

    def check_friendship(self, user_ids: list[int] | int, need_sign: bool = False,
                         extended: bool = False) -> Coroutine[Any, Any, list[Friendship]]:
        params = {}

        for user_id in user_ids:
            if user_id <= 0:
                raise InvalidUserID(user_id)
            params["user_ids"] += f",{user_id}" if len(params["user_ids"]) != 0 else user_id

        params["need_sign"] = need_sign
        params["extended"] = extended

        return self.request_async("friends.areFriends", params)

    def delete(self, user_id: int) -> Coroutine[Any, Any, object]:
        if user_id <= 0:
            raise InvalidUserID(user_id)
        params = {"user_id": user_id}
        return self.request_async("friends.delete", params)

    def read_all_requests(self) -> Coroutine[Any, Any, None]:
        params = {}
        return self.request_async("friends.deleteAllRequests", params)

    def delete_list(self, list_id: int) -> Coroutine[Any, Any, None]:
        if list_id < 0:
            raise NegativeValueError("list_id", list_id
                                     )
        params = {
            "list_id": list_id
        }
        return self.request_async("friends.deleteList", params)

    def edit_users_list(self, user_id: int, list_ids: list[int] = None) -> Coroutine[Any, Any, None]:
        if user_id <= 0:
            raise InvalidUserID(user_id)

        params = {
            "user_id": user_id
        }
        if list_ids:
            for list_id in list_ids:
                if list_id < 0:
                    raise NegativeValueError("list_id", list_id)
                params["list_ids"] += f",{list_id}" if len(params["list_ids"]) != 0 else list_id

        return self.request_async("friends.edit", params)

    def edit_list(self, list_id: int, name: str = None, user_ids: list[int] = None,
                  add_user_ids: list[int] = None,
                  delete_user_ids: list[int] = None) -> Coroutine[Any, Any, None]:
        params = {}

        if list_id < 0:
            raise NegativeValueError("list_id", list_id)

        if name:
            params["name"] = name
        if user_ids:
            params["user_ids"] = ','.join(user_ids)
        if add_user_ids:
            params["add_user_ids"] = ','.join(add_user_ids)
        if delete_user_ids:
            params["delete_user_ids"] = ','.join(delete_user_ids)

        return self.request_async("friends.editList", params)

    def get(self, user_id: int = None, order: FriendsOrder | str = None, list_id: int = None,
            count: int = None, offset: int = None, fields: list[UserFields] | str = None,
            name_case: str = "nom", ref: str = None) -> Coroutine[Any, Any, list[int] | list[User]]:
        params = {}

        if user_id:
            if user_id < 0:
                raise InvalidUserID(user_id)
            params["user_id"] = user_id

        if order:
            if isinstance(order, FriendsOrder):
                params["order"] = order.value
            else:
                params["order"] = order

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if list_id:
            if list_id < 0:
                raise NegativeValueError("list_id", list_id)
            params["list_id"] = list_id
        if fields:
            if isinstance(fields, list):
                params["fields"] = ','.join(field.value for field in fields)
            else:
                params["fields"] = fields
        if name_case:
            params["name_case"] = name_case
        if ref:
            if len(ref) > 255:
                raise UndefinedParameterValue("ref", ref)
            params["ref"] = ref

        return self.request_async("friends.get", params)

    def get_my(self, order: FriendsOrder | str = None, list_id: int = None,
               count: int = None, offset: int = None, fields: list[UserFields] | str = None,
               name_case: str = "nom", ref: str = None) -> Coroutine[Any, Any, list[int] | list[User]]:
        params = {}

        if order:
            if isinstance(order, FriendsOrder):
                params["order"] = order.value
            else:
                params["order"] = order

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if list_id:
            if list_id < 0:
                raise NegativeValueError("list_id", list_id)
            params["list_id"] = list_id
        if fields:
            if isinstance(fields, list):
                params["fields"] = ','.join(field.value for field in fields)
            else:
                params["fields"] = fields
        if name_case:
            params["name_case"] = name_case
        if ref:
            if len(ref) > 255:
                raise UndefinedParameterValue("ref", ref)
            params["ref"] = ref

        return self.request_async("friends.get", params)

    def get_app_users(self) -> Coroutine[Any, Any, list[int]]:
        params = {}
        return self.request_async("friends.getAppUsers", params)

    def get_lists(self, user_id: int = None,
                  return_system: bool = True) -> Coroutine[Any, Any, list[FriendList]]:
        params = {}

        if user_id <= 0:
            raise InvalidUserID(user_id)

        params["user_id"] = user_id
        params["return_system"] = return_system

        return self.request_async("friends.getLists", params)

    def get_my_lists(self, return_system: bool = True) -> Coroutine[Any, Any, list[FriendList]]:
        params = {"return_system": return_system}

        return self.request_async("friends.getLists", params)

    def get_mutual(self, source_user_id: int, target_user_id: int | list[int],
                   order: FriendsOrder | str = None, count: int = None,
                   offset: int = None, need_common_count: bool = False) -> Coroutine[Any, Any, list[MutualFriend]]:
        if source_user_id <= 0:
            raise InvalidUserID(source_user_id)
        params = {"source_uid": source_user_id}

        if isinstance(target_user_id, list):
            for target_uid in target_user_id:
                if target_uid <= 0:
                    raise InvalidUserID(target_uid)
                params["target_uids"] += f",{target_uid}" if len(params["target_uids"]) != 0 else target_uid
        else:
            params["target_uid"] = target_user_id

        if order:
            if isinstance(order, FriendsOrder):
                params["order"] = order.value
            else:
                params["order"] = order

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        params["need_common_count"] = need_common_count

        return self.request_async("friends.getMutual", params)

    def get_my_mutual(self, target_user_id: int | list[int], order: FriendsOrder | str = None,
                      count: int = None, offset: int = None,
                      need_common_count: bool = False) -> Coroutine[Any, Any, list[MutualFriend]]:
        params = {}

        if isinstance(target_user_id, list):
            for target_uid in target_user_id:
                if target_uid <= 0:
                    raise InvalidUserID(target_uid)
                params["target_uids"] += f",{target_uid}" if len(params["target_uids"]) != 0 else target_uid
        else:
            params["target_uid"] = target_user_id

        if order:
            if isinstance(order, FriendsOrder):
                params["order"] = order.value
            else:
                params["order"] = order

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        params["need_common_count"] = need_common_count

        return self.request_async("friends.getMutual", params)

    def get_online(self, user_id: int = None, list_id: int = None, online_mobile: bool = None,
                   order: FriendsOrder | str = None, count: int = None,
                   offset: int = None) -> Coroutine[Any, Any, list[int]]:
        params = {}

        if user_id:
            if user_id <= 0:
                raise InvalidUserID(user_id)
            params["user_id"] = user_id
        if list_id:
            if list_id < 0:
                raise NegativeValueError("list_id", list_id)
            params["list_id"] = list_id

        if online_mobile:
            params["online_mobile"] = online_mobile

        if order:
            params["order"] = order
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        return self.request_async("friends.getOnline", params)

    def get_my_online(self, list_id: int = None, online_mobile: bool = None,
                      order: FriendsOrder | str = None, count: int = None,
                      offset: int = None) -> Coroutine[Any, Any, list[int]]:
        params = {}

        if list_id:
            if list_id < 0:
                raise NegativeValueError("list_id", list_id)
            params["list_id"] = list_id

        if online_mobile:
            params["online_mobile"] = online_mobile

        if order:
            params["order"] = order
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        return self.request_async("friends.getOnline", params)

    def get_my_recent(self, count: int = None) -> Coroutine[Any, Any, list[int]]:
        params = {}
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        return self.request_async("friends.getRecent", params)

    def get_my_requests(
            self, count: int = None, offset: int = None, extended: bool = False,
            need_mutual: bool = False, outgoing: bool = False,
            sort: int = None, need_viewed: bool = False,
            suggested: bool = False, ref: str = None,
            fields: list[UserFields] | str = None
    ) -> Coroutine[Any, Any, list[int] | list[User] | list[(User, MutualFriend)]]:
        params = {}

        if offset < 0:
            raise NegativeValueError("offset", offset)
        params["offset"] = offset

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        params["extended"] = extended
        params["need_mutual"] = need_mutual
        params["out"] = outgoing

        if outgoing:
            if sort is not None:
                if sort == 0 or sort == 1:
                    params["sort"] = sort
                else:
                    raise UndefinedParameterValue("sort", sort)
            params["need_viewed"] = need_viewed

        params["suggested"] = suggested

        if ref:
            if len(ref) > 255:
                raise UndefinedParameterValue("ref", ref)
            params["ref"] = ref

        if fields:
            if isinstance(fields, list):
                params["fields"] = ','.join(field.value for field in fields)
            else:
                params["fields"] = fields

        return self.request_async("friends.getRequests", params)

    def get_my_suggestions(self, count: int = None, offset: int = None,
                           fields: list[UserFields] | str = None, name_case: str = "nom",
                           with_many_mutual: bool = False) -> Coroutine[Any, Any, list[User]]:
        params = {}

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        if fields:
            if isinstance(fields, list):
                params["fields"] = ','.join(field.value for field in fields)
            else:
                params["fields"] = fields

        params["name_case"] = name_case

        if with_many_mutual:
            params["filter"] = "mutual"

        return self.request_async("friends.getSuggestions", params)

    def search(self, user_id: int = None, text: str = None, fields: list[UserFields] | str = None,
               name_case: str = "nom", offset: int = None,
               count: int = None) -> Coroutine[Any, Any, list[User]]:
        params = {}
        if user_id:
            if user_id <= 0:
                raise InvalidUserID(user_id)
            params["user_id"] = user_id

        params["text"] = text

        if fields:
            if isinstance(fields, list):
                params["fields"] = ','.join(field.value for field in fields)
            else:
                params["fields"] = fields

        params["name_case"] = name_case

        if offset < 0:
            raise NegativeValueError("offset", offset)
        params["offset"] = offset

        if count < 0:
            raise NegativeValueError("count", count)
        params["count"] = count

        return self.request_async("friends.search", params)
