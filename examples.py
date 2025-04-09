from client import ViKoClient
from config import user_token

# user_token = "INSERT_YOUR_TOKEN_HERE"

vk_client = ViKoClient(api_token=user_token)


async def status_tests():
    self_status = await vk_client.status.get_my()  # get your status
    others_status = await vk_client.status.get(user_id=1234)  # get users_status
    group_status = await vk_client.status.get(group_id=1234)  # or get groups status

    # you can simply change your status
    await vk_client.status.set(text="I'm the new status!")

    # or change group status, where you have rights to
    await vk_client.status.set(text="I'm the new group status!", group_id=1234)


async def wall_tests():
    wall_posts = await vk_client.wall.get_posts()  # get your wall
    other_wall_posts = await vk_client.wall.get_posts(owner_id=1234)  # get users wall

    comments = await vk_client.wall.get_comments(owner_id=1234, post_id=123)  # get comments

    posts = await vk_client.wall.search(q="kinda text")  # search on your wall

    await vk_client.wall.pin(post_id=123)  # pin something on your wall
    await vk_client.wall.unpin(post_id=123)  # and simply unpin it

    await vk_client.wall.delete(post_id=123)  # delete post from your wall
    await vk_client.wall.delete_comment(comment_id=123)  # or comment


async def docs_tests():
    # you can simply get all your docs
    files = await vk_client.docs.get()

    # or get by id
    files = await vk_client.docs.get_by_id(file_links=[(12345, 123), (12345, 125)])

    # you can also get docs from global search
    files = await vk_client.docs.search(q="Python", count=5)


async def friends_test():
    suggestions = await vk_client.friends.get_my_suggestions(count=5)  # get first 5 friend suggestions


async def likes_test():
    is_liked = await vk_client.likes.check_post(post_id=2431591, owner_id=1)
    likes = await vk_client.likes.get(object_type="post", item_id=2431591, owner_id=1)


import asyncio
asyncio.run(docs_tests())


