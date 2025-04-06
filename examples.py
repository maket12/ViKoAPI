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
    wall_posts = await vk_client.wall.get()  # get your wall
    other_wall_posts = await vk_client.wall.get(owner_id=1234)  # get users wall


async def friends_test():
    suggestions = await vk_client.friends.get_my_suggestions(count=5)  # get first 5 friend suggestions


async def likes_test():
    # is_liked = await vk_client.likes.check_post(post_id=2431591, owner_id=1)
    likes = await vk_client.likes.get(object_type="post", item_id=2431591, owner_id=1)
    print(likes)
    print(len(likes))


async def user_test():
    posts = await vk_client.wall.get_posts()
    for post in posts:
        print(post.reposts_history[0].attachments)
        print('\n')
        print(post.to_dict())
        print('\n')
        print('\n')
    # friends = await vk_client.friends.get_my_recent()
    # print(friends)
    # gifts = await vk_client.gifts.get_my(count=5)

    # for gif in gifts:
    #     print(gif.datetime)


import asyncio
asyncio.run(likes_test())


