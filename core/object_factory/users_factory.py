from core.object_factory.groups_factory import GroupsFactory
from vk_types.user.User import User


class UsersFactory:
    @staticmethod
    def create_user(data: dict) -> User:
        return User(**data)

    @staticmethod
    def create_users(items: list) -> list[User]:
        result = []
        for item in items:
            user = UsersFactory.create_user(item)
            result.append(user)
        return result

    @staticmethod
    def create_subscriptions(items: list):
        users = []
        groups = []

        for item in items:
            if item["type"] == "profile":
                user = UsersFactory.create_user(item)
                users.append(user)
            else:
                group = GroupsFactory.create_group(item)
                groups.append(group)

        return users, groups
