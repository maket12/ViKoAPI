import webbrowser
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

    def __init__(self, api_token: str | None = None, proxy: str | None = None, api_version: str = "5.199"):
        """
        :param api_token: Your access_token
        :param proxy: Your proxy in ? -- format: ip:login:password -- ?
        :param api_version: Don't change it! Methods can be not working!
        """
        self.version = 0.34
        self.api_token = api_token
        self.proxy = proxy
        self.api_version = api_version
        self.middleware = None
        self._proxy_checked = False

        self._authorize()

    def _authorize(self):
        def welcome_info():
            title = f"ViKoAPI {self.version}"
            padding = 4
            width = len(title) + padding * 2
            border = "#" * (width + 4)
            content_line = f"# {' ' * padding}{title}{' ' * padding} #"

            print(border)
            print(content_line)
            print(border)

        def auth_info():
            import time

            time.sleep(3)
            print("\nYou will be redirected on unofficial page to get api-key.")
            time.sleep(2)
            print("Be sure that you choose correct option. It will depend how many methods you can call on which "
                  "option you choose.")
            print("Recommended: \"VK Admin\", \"vk.com\".\n")
            time.sleep(4)

            for i in range(5, 0, -1):
                print(f"\rRedirecting in {i}...", end="", flush=True)
                time.sleep(1)

        welcome_info()
        if not self.api_token:
            auth_info()
            webbrowser.open(url="https://vkhost.github.io")
            self.api_token = input("\rEnter your api-token: ")

    async def _ensure_proxy(self):
        if self.proxy and not self._proxy_checked:
            is_ok = await self.check_proxy()
            if not is_ok:
                raise ConnectionError("Proxy check failed: cannot reach test URL.")
            self._proxy_checked = True

    async def check_proxy(self, test_url: str = "https://www.google.com", timeout: int = 10) -> bool:
        try:
            connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(test_url, proxy=self.proxy, timeout=timeout) as response:
                    if response.status == 200:
                        return True
                    else:
                        raise False
        except Exception:
            raise False

    def set_middleware(self, middleware: ResponseMiddleware):
        self.middleware = middleware

    async def _async_request(self, method: str, params: dict):
        await self._ensure_proxy()
        async with aiohttp.ClientSession(proxy=self.proxy) as session:
            params.update({
                "access_token": self.api_token,
                "v": self.api_version
            })
            async with session.get(self.BASE_URL + method, params=params) as response:
                data = await response.json()
                return self.middleware.process(method, data) if self.middleware else data
