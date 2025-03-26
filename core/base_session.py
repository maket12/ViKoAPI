import requests
import aiohttp
from core.response_middleware import ResponseMiddleware


class BaseSession:
    """
        Сначала получить client_id:
            1)Создать приложение(https://id.vk.com/about/business/go/accounts/198504/apps)
            2)Получить client_id(указывается в поисковой строке при выборе определённого приложения)
        Далее вызвать метод authorize(), чтобы получить access_token
        """
    BASE_URL = "https://api.vk.com/method/"
    OAUTH_URL = "https://oauth.vk.com/authorize"

    def __init__(self, api_token: str, proxy: str = None, api_version: str = "5.199"):
        """
        :param api_token: Your access_token
        :param proxy: Your proxy in ? -- format: ip:login:password -- ?
        :param api_version: Don't change it! Methods can be not working!
        """
        self.api_token = api_token
        self.proxy = proxy
        self.api_version = api_version
        self.middleware = None

        if self.proxy:
            self.check_proxy()

    async def check_proxy(self, test_url: str = "https://www.google.com", timeout: int = 10):
        try:
            connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(test_url, proxy=self.proxy, timeout=timeout) as response:
                    if response.status == 200:
                        return "ok"
                    else:
                        raise ConnectionError
        except Exception:
            raise ConnectionError

    def set_middleware(self, middleware: ResponseMiddleware):
        self.middleware = middleware

    # def _sync_request(self, method: str, params: dict):
    #     params.update({"access_token": self.api_token, "v": self.api_version})
    #     response = requests.get(self.BASE_URL + method, params=params)
    #     return response.json()

    async def _async_request(self, method: str, params: dict):
        async with aiohttp.ClientSession(proxy=self.proxy) as session:
            params.update({"access_token": self.api_token, "v": self.api_version})
            async with session.get(self.BASE_URL + method, params=params) as response:
                data = await response.json()
                return self.middleware.process(method, data) if self.middleware else data
