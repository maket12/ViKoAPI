from vk_types.user.User import User
from vk_types.chat.Chat import Chat
from vk_types.post.Post import (
        Post, PostsCopyright, PostsLikes,
        PostsComments, PostsReposts, PostsGeo, PostsSource)
from vk_types.post.post_attributes.Place import GeoPlace
from vk_types.post.post_attributes.Donut import PostsDonut
from vk_types.gift_item.GiftItem import GiftItem, Gift
from vk_types.friends.friendship.Friendship import Friendship
from vk_types.friends.friend_list.FriendList import FriendList
from vk_types.friends.mutual_friend.MutualFriend import MutualFriend


class ObjectFactory:
    @staticmethod
    def create_user(data: dict) -> User:
        mapped_data = {
            "found_with": data.get("found_with")
        }
        return User(**mapped_data)

    @staticmethod
    def create_users(items: list) -> list[User]:
        result = []
        for item in items:
            user = ObjectFactory.create_user(item)
            result.append(user)
        return result

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
        result = []
        for item in items:
            friendship = ObjectFactory.create_friendship(item)
            result.append(friendship)
        return result

    @staticmethod
    def create_friend_list(data: dict) -> FriendList:
        mapped_data = {
            "name": data.get("name"),
            "list_id": data.get("id")
        }
        return FriendList(**mapped_data)

    @staticmethod
    def create_friend_lists(items: list) -> list[FriendList]:
        result = []
        for item in items:
            friend_list = ObjectFactory.create_friend_list(item)
            result.append(friend_list)
        return result

    @staticmethod
    def create_friend_requests(items: list) -> list[int] | list[User] | list[(User, list[MutualFriend])]:
        result = []

        if items:
            if isinstance(items[0], int):
                return items
            for request in items:
                user = ObjectFactory.create_user(request)
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

    @staticmethod
    def create_group(data: dict) -> str:return ""

    @staticmethod
    def create_comments(data: dict) -> PostsComments:
        mapped_data = {
            "count": data.get("count"),
            "can_post": data.get("can_post"),
            "groups_can_post": data.get("groups_can_post"),
            "can_close": data.get("can_close"),
            "can_open": data.get("can_open")
        }
        return PostsComments(**mapped_data)

    @staticmethod
    def create_copyright(data: dict) -> PostsCopyright:
        mapped_data = {
            "source_id": data.get("id"),
            "source_link": data.get("link"),
            "source_name": data.get("name"),
            "source_type": data.get("type")
        }
        return PostsCopyright(**mapped_data)

    @staticmethod
    def create_likes(data: dict) -> PostsLikes:
        mapped_data = {
            "count": data.get("count"),
            "is_liked": data.get("user_likes"),
            "can_like": data.get("can_like"),
            "can_repost": data.get("can_publish")
        }
        return PostsLikes(**mapped_data)

    @staticmethod
    def create_reposts(data: dict) -> PostsReposts:
        mapped_data = {
            "count": data.get("count"),
            "is_reposted": data.get("user_reposted")
        }
        return PostsReposts(**mapped_data)

    @staticmethod
    def create_post_source(data: dict) -> PostsSource:
        mapped_data = {
            "source_type": data.get("type"),
            "platform": data.get("platform"),
            "data": data.get("data"),
            "url": data.get("url")
        }
        return PostsSource(**mapped_data)

    @staticmethod
    def create_place(data: dict) -> GeoPlace:
        mapped_data = {
            "place_id": data.get("id"),
            "title": data.get("title"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "created_unix": data.get("created"),
            "icon": data.get("icon"),
            "checkins": data.get("checkins"),
            "updated_unix": data.get("updated"),
            "place_type": data.get("type"),
            "city": data.get("city"),
            "address": data.get("address")
        }
        return GeoPlace(**mapped_data)

    @staticmethod
    def create_geo(data: dict) -> PostsGeo:
        mapped_data = {
            "place_type": data.get("type"),
            "coordinates": data.get("coordinates"),
            "place": ObjectFactory.create_place(data.get("place")) if data.get("place") else None
        }
        return PostsGeo(**mapped_data)

    @staticmethod
    def create_post_donut(data: dict) -> PostsDonut:
        mapped_data = {
            "is_donut": data.get("is_donut"),
            "paid_duration": data.get("paid_duration"),
            "placeholder": data.get("placeholder"),
            "can_publish_free_copy": data.get("can_publish_free_copy"),
            "edit_mode": data.get("edit_mode")
        }
        return PostsDonut(**mapped_data)

    @staticmethod
    def create_post(data: dict) -> Post:
        mapped_data = {
            "post_id": data.get("id"),
            "owner_user_id": data.get("owner_id"),
            "from_user_id": data.get("from_id"),
            "created_by_user_id": data.get("created_by"),
            "date_unix": data.get("date"),
            "text": data.get("text"),
            "reply_owner_user_id": data.get("reply_owner_id"),
            "reply_post_id": data.get("reply_post_id"),
            "for_friends_only": data.get("friends_only"),
            "comments": ObjectFactory.create_comments(data.get("comments")) if data.get("comments") else None,
            "copyright": ObjectFactory.create_copyright(data.get("copyright")),
            "likes": ObjectFactory.create_likes(data.get("likes")) if data.get("likes") else None,
            "reposts": ObjectFactory.create_reposts(data.get("reposts")) if data.get("reposts") else None,
            "views": data.get("views").get("count"),
            "post_type": data.get("post_type"),
            "post_source": ObjectFactory.create_post_source(data.get("post_source")),
            "attachments": data.get("attachments"),
            "geo": ObjectFactory.create_geo(data.get("geo")) if data.get("geo") else None,
            "signer_user_id": data.get("signer_id"),
            "reposts_history": ObjectFactory.create_posts(data.get("copy_history")) if data.get("copy_history") else None,
            "can_pin": data.get("can_pin"),
            "can_delete": data.get("can_delete"),
            "can_edit": data.get("can_edit"),
            "is_pinned": data.get("is_pinned"),
            "is_favorite": data.get("is_favorite"),
            "is_add": data.get("marked_as_ads"),
            "donut": ObjectFactory.create_post_donut(data.get("donut")) if data.get("donut") else None,
            "postponed_id": data.get("postponed_id")
        }
        return Post(**mapped_data)

    @staticmethod
    def create_posts(items: list) -> list[Post]:
        result = []
        for item in items:
            post = ObjectFactory.create_post(item)
            result.append(post)
        return result

    @staticmethod
    def create_chat(data: dict) -> Chat:
        mapped_data = {
            "chat_id": data.get("id"),
            "chat_type": data.get("type"),
            "title": data.get("title"),
            "admin_user_id": data.get("admin_id"),
            "users": data.get("users"),
            "push_settings": data.get("push_settings"),
            "photo_50": data.get("photo_50"),
            "photo_100": data.get("photo_100"),
            "photo_200": data.get("photo_200"),
            "photo_base": data.get("photo_base"),
            "was_left": bool(data.get("left")),
            "was_kicked": bool(data.get("kicked"))
        }
        return Chat(**mapped_data)

    @staticmethod
    def create_gift_items(items: list) -> list[GiftItem]:
        result = []
        for item in items:
            gift_item = ObjectFactory.create_gift_item(item)
            result.append(gift_item)
        return result

    @staticmethod
    def create_gift_item(data: dict) -> GiftItem:
        mapped_data = {
            "gift_item_id": data.get("id"),
            "from_user_id": data.get("from_id"),
            "message": data.get("message"),
            "unix_date": data.get("date"),
            "gift": ObjectFactory.create_gift(data.get("gift")),
            "privacy": data.get("privacy")
        }
        return GiftItem(**mapped_data)

    @staticmethod
    def create_gift(data: dict) -> Gift:
        mapped_data = {
            "gift_id": data.get("id"),
            "thumb_256": data.get("thumb_256"),
            "thumb_96": data.get("thumb_96"),
            "thumb_48": data.get("thumb_48")
        }
        return Gift(**mapped_data)
