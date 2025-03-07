from client import ViKoClient

user_token = "INSERT_YOUR_TOKEN_HERE"

vk_client = ViKoClient(api_token=user_token)


async def status_tests():
    self_status = await vk_client.status.get()  # get your status
    others_status = await vk_client.status.get(user_id="some_uid")  # get users_status
    group_status = await vk_client.status.get(group_id="some_uid")  # or get groups status

    # you can simply change your status
    await vk_client.status.set(text="I'm the new status!")

    # or change group status, where you have rights to
    await vk_client.status.set(text="I'm the new group status!", group_id="some_uid")


async def wall_test():
    wall_posts = await vk_client.wall.get()  # get your wall
    other_wall_posts = await vk_client.wall.get(owner_id="some_uid")  # get users_status


