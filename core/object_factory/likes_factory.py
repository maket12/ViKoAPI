from core.object_factory.users_factory import UsersFactory
from vk_types.user.User import User
from vk_types.reaction.Reaction import Reaction


class LikesFactory:
    @staticmethod
    def create_reaction(data: dict) -> Reaction:
        mapped_data = {
            "reaction_id": data.get("id"),
            "count": data.get("count")
        }
        return Reaction(**mapped_data)

    @staticmethod
    def create_reactions(items: list) -> list[Reaction]:
        return [LikesFactory.create_reaction(item) for item in items]

    @staticmethod
    def create_likes_list(items: list) -> list[int] | list[User]:
        result = []
        if isinstance(items[0], int):
            return items
        else:
            for item in items:
                user = UsersFactory.create_user(item)
                result.append(user)
        return result
