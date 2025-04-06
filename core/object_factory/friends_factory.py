from core.object_factory.users_factory import UsersFactory
from vk_types.user.User import User
from vk_types.friends.friendship.Friendship import Friendship
from vk_types.friends.friend_list.FriendList import FriendList
from vk_types.friends.mutual_friend.MutualFriend import MutualFriend


class FriendsFactory:
    @staticmethod
    def create_online_friends(data: dict | list[int]) -> list[int]:
        if isinstance(data, list):
            return data

        result = []

        online_friends = data.get("online")
        online_mobile_friends = data.get("online_mobile")
        if online_friends or online_mobile_friends:
            for online_friend in online_friends:
                result.append(online_friend)

            for online_mobile_friend in online_mobile_friends:
                result.append(online_mobile_friend)
        return result

    @staticmethod
    def create_friendship(data: dict) -> Friendship:
        mapped_data = {
            "user_id": data.get("user_id"),
            "status": data.get("friend_status"),
            "is_request_unread": data.get("is_request_unread")
        }
        return Friendship(**mapped_data)

    @staticmethod
    def create_friendships(items: list) -> list[Friendship]:
        return [FriendsFactory.create_friendship(item) for item in items]

    @staticmethod
    def create_friend_list(data: dict) -> FriendList:
        mapped_data = {
            "name": data.get("name"),
            "list_id": data.get("id")
        }
        return FriendList(**mapped_data)

    @staticmethod
    def create_friend_lists(items: list) -> list[FriendList]:
        return [FriendsFactory.create_friend_list(item) for item in items]

    @staticmethod
    def create_friend_requests(items: list) -> list[int] | list[User] | list[(User, list[MutualFriend])]:
        result = []

        if items:
            if isinstance(items[0], int):
                return items
            for request in items:
                user = UsersFactory.create_user(request)
                mutual = request.get("mutual")
                source_user_id = request.get("user_id")

                if mutual and mutual.get("users"):
                    mutual_friends = []

                    for user_id in mutual.get("users"):
                        mutual_friend = MutualFriend(user_id, source_user_id, None)
                        mutual_friends.append(mutual_friend)

                    request_tuple = (user, mutual_friends)
                    result.append(request_tuple)
                else:
                    result.append(user)

        return result

    @staticmethod
    def create_mutual_friends(data: list | list[dict]) -> list[MutualFriend]:
        result = []
        if isinstance(data, list):
            for mutual_uid in data:
                mutual_friend = MutualFriend(mutual_uid, None, None)
                result.append(mutual_friend)
        else:
            for mutual_data in data:
                mutual_friends_ids = mutual_data.get("common_friends")
                target_user_id = mutual_data.get("id")
                for mutual_friend_id in mutual_friends_ids:
                    mutual_friend = MutualFriend(mutual_friend_id, None, target_user_id)
                    result.append(mutual_friend)
        return result

