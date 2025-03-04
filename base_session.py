import requests
import aiohttp


class BaseSession:
    """
        version = 0.01
        Сначала получить client_id:
            1)Создать приложение(https://id.vk.com/about/business/go/accounts/198504/apps)
            2)Получить client_id(указывается в поисковой строке при выборе определённого приложения)
        Далее вызвать метод authorize(), чтобы получить access_token
        """
    BASE_URL = "https://api.vk.com/method/"

    def __init__(self, api_token: str, api_version: str = "5.199"):
        self.api_token = api_token
        self.api_version = api_version

    def _sync_request(self, method: str, params: dict):
        params.update({"access_token": self.api_token, "v": self.api_version})
        response = requests.get(self.BASE_URL + method, params=params)
        return response.json()

    async def _async_request(self, method: str, params: dict):
        async with aiohttp.ClientSession() as session:
            params.update({"access_token": self.api_token, "v": self.api_version})
            async with session.get(self.BASE_URL + method, params=params) as response:
                return await response.json()