from typing import overload, Literal, Union, Any, List
import json
from core.object_factory import ObjectFactory
from errors.exceptions import *  # maybe replace and do 2 files with exceptions: response's and before response
from vk_types.gift_item import GiftItem


class ResponseMiddleware:
    """
       Middleware для обработки API-ответов и автоматического преобразования JSON в объекты.
    """
    def __init__(self, object_factory: ObjectFactory):
        self.object_factory = object_factory

    def process(self, method: str, response: dict):
        """
            Обрабатывает ответ API, автоматически конвертируя в объекты, если метод поддерживается.
        """
        if "error" in response:
            error = response["error"]
            error_code = error.get("error_code")
            error_msg = error.get("error_msg")
            request_params = error.get("request_params")

            match error_code:
                case 1:
                    raise UnknownError(error_msg=error_msg, request_params=request_params)
                case 2:
                    raise ApiAppOffError(error_msg=error_msg, request_params=request_params)
                case 5:
                    raise AuthorisationError(error_msg=error_msg, request_params=request_params)
                case 6:
                    raise RateLimitError(error_msg=error_msg, request_params=request_params)
                case 9:
                    raise ActionLimitError(error_msg=error_msg, request_params=request_params)
                case 10:
                    raise InternalServerError(error_msg=error_msg, request_params=request_params)
                case 11:
                    raise TestAppError(error_msg=error_msg, request_params=request_params)
                case 18:
                    raise ProfileDeletedError(error_msg=error_msg, request_params=request_params)
                case 19:
                    raise ContentBlockedError(error_msg=error_msg, request_params=request_params)
                case 23:
                    raise MethodUnavailableError(error_msg=error_msg, request_params=request_params)
                case 30:
                    raise PrivateProfileError(error_msg=error_msg, request_params=request_params)
                case 203:
                    raise GroupAccessError(error_msg=error_msg, request_params=request_params)
                case _:
                    raise ViKoAPIResponseError(error_code=error_code, error_msg=error_msg,
                                               request_params=request_params)
        if "response" in response:
            data = response["response"]

            return self._convert_object(method, data)
        return response

    def _convert_object(self, method: str, data: json):
        """
            Определяет, в какой объект конвертировать JSON-ответ, основываясь на методе API.
        """
        match method:
            case "status.get":
                return data["text"]
            case "groups.search":
                return
            case "wall.get":
                return self.object_factory.create_posts(data.get("items"))
            case "gifts.get":
                return self.object_factory.create_gift_items(data.get("items"))
            case _:
                return data
