from client import ViKoClient


vk_client = ViKoClient(api_token=user_token)

import asyncio
# print(asyncio.run(vk_client.get_status(213904939)))

import requests


response = requests.get(
    "https://api.vk.com/method/status.get",
    params={"access_token": ACCESS_TOKEN, "v": "5.191"}
)

print(response.json())

