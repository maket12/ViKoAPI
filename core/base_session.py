import requests
import aiohttp
import webbrowser
import base64
from core.response_middleware import ResponseMiddleware
from errors.exceptions import ClientParamsEmpty


class BaseSession:
    """
        Сначала получить client_id:
            1)Создать приложение(https://id.vk.com/about/business/go/accounts/198504/apps)
            2)Получить client_id(указывается в поисковой строке при выборе определённого приложения)
        Далее вызвать метод authorize(), чтобы получить access_token
        """
    BASE_URL = "https://api.vk.com/method/"
    OAUTH_URL = "https://oauth.vk.com/authorize"

    def __init__(self, api_token: str, api_version: str = "5.199"):
        """
        :param api_token: Your access_token
        :param api_version: Don't change it! Methods can be not working!
        """
        self.api_token = api_token
        self.api_version = api_version
        self.middleware = None

        # self._check_api_token()

    # def _save_token(self):
    #     session_filename = "ViKoSession.bin"
    #     encoded_token = base64.b64encode(self.api_token.encode())
    #     with open(session_filename, "wb") as session:
    #         session.write(encoded_token)
    #
    # def _load_token(self):
    #     with open(self.api_token, "rb") as session:
    #         decoded_token = base64.b64decode(session.read()).decode()
    #         self.api_token = decoded_token

    # def _check_api_token(self):
    #     if not self.api_token:
    #         if not self.vk_login or not self.vk_password:
    #             raise ClientParamsEmpty
    #         self._authorize()
    #
    #     self._load_token()

    # def _authorize(self,
    #                scopes: str = "offline,friends,photos,audio,video,stories,pages,menu,status,"
    #                              "notes,messages,wall,ads,docs,groups,notifications,stats,email,"
    #                              "market,phone_number,notify"):
    #     """Авторизация через OAuth: открывает браузер, получает токен и автоматически сохраняет его."""
    #
    #     # Открываем ссылку в браузере
    #     auth_url = ("https://oauth.vk.com/oauth/authorize?"
    #                 "client_id=6287487&scope=1073737727&"
    #                 "redirect_uri=https://oauth.vk.com/blank.html&"
    #                 "display=page&response_type=token&revoke=1&"
    #                 "slogin_h=697539d4c2a09a7104.b7ee5c97219eb5a66e&no_session=1")
    #
    #     try:
    #         print("Welcome to ViKoAPI framework - an open-source async tool for VK API.\n")
    #         if isinstance(self.api_token, str) and len(self.api_token) > 12:
    #             self._save_token()
    #             print("\nYour session file was created successful.\n")
    #     except KeyboardInterrupt:
    #         print("The authorization process was cancelled.")
    #         return

    def set_middleware(self, middleware: ResponseMiddleware):
        self.middleware = middleware

    def _sync_request(self, method: str, params: dict):
        params.update({"access_token": self.api_token, "v": self.api_version})
        response = requests.get(self.BASE_URL + method, params=params)
        return response.json()

    async def _async_request(self, method: str, params: dict):
        async with aiohttp.ClientSession() as session:
            params.update({"access_token": self.api_token, "v": self.api_version})
            async with session.get(self.BASE_URL + method, params=params) as response:
                data = await response.json()
                return self.middleware.process(method, data) if self.middleware else data
