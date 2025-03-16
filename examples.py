from client import ViKoClient

# user_token = "INSERT_YOUR_TOKEN_HERE"

user_token = "vk1.a.CLHIYVRhdmT7S9mvXQbTI8oKFQL5xuqRV-VISc95hIqnVYha42fEwfFfTdu4mj4Kb1sOwbadgv5VOgFy0p7byKuN6TsUjDnhhJNFZkJ2qm0TA4offInyOWgfPqSfek3iX1xQD9_HBJWvHqPNC8-kWobphPTudAqywofPea3dX2GWLATKrDIunk4nrepiUR2CqguCBiCBNbk4mwjwbZ32Q"

vk_client = ViKoClient(api_token=user_token)


async def status_tests():
    self_status = await vk_client.status.get_my()  # get your status
    others_status = await vk_client.status.get(user_id="some_uid")  # get users_status
    group_status = await vk_client.status.get(group_id="some_uid")  # or get groups status

    # you can simply change your status
    await vk_client.status.set(text="I'm the new status!")

    # or change group status, where you have rights to
    await vk_client.status.set(text="I'm the new group status!", group_id="some_group_id")


async def wall_test():
    wall_posts = await vk_client.wall.get()  # get your wall
    other_wall_posts = await vk_client.wall.get(owner_id="some_uid")  # get users_status


async def user_test():
    status = await vk_client.status.get_my()
    print(status)

import asyncio
asyncio.run(user_test())


