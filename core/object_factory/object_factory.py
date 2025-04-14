from core.object_factory.users_factory import UsersFactory
from core.object_factory.friends_factory import FriendsFactory
from core.object_factory.likes_factory import LikesFactory
from core.object_factory.groups_factory import GroupsFactory
from core.object_factory.attachments_factory import AttachmentsFactory
from core.object_factory.posts_factory import PostsFactory
from core.object_factory.comments_factory import CommentsFactory
from core.object_factory.chats_factory import ChatsFactory
from core.object_factory.albums_factory import AlbumsFactory


class ObjectFactory:
    def __init__(self):
        self.user = UsersFactory()
        self.friends = FriendsFactory()
        self.likes = LikesFactory()
        self.groups = GroupsFactory()
        self.attachments = AttachmentsFactory()
        self.post = PostsFactory()
        self.comments = CommentsFactory()
        self.chats = ChatsFactory()
        self.albums = AlbumsFactory()
