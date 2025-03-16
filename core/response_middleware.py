import json
from core.object_factory import ObjectFactory
from errors.exceptions import *  # maybe replace and do 2 files with exceptions: response's and before response


class ResponseMiddleware:
    """
       Middleware для обработки API-ответов и автоматического преобразования JSON в объекты.
    """
    def __init__(self, object_factory: ObjectFactory):
        self.object_factory = object_factory

    def process(self, method: str, response: json):
        """
            Обрабатывает ответ API, автоматически конвертируя в объекты, если метод поддерживается.
        """
        if "error" in response:
            error = response["error"]
            error_code = error.get("error_code")
            error_msg = error.get("error_msg")
            request_params = error.get("request_params")

            if error_code == 1:
                raise UnknownError(error_msg=error_msg, request_params=request_params)
            elif error_code == 2:
                raise ApiAppOffError(error_msg=error_msg, request_params=request_params)
            elif error_code == 5:
                raise AuthorisationError(error_msg=error_msg, request_params=request_params)
            elif error_code == 6:
                raise RateLimitError(error_msg=error_msg, request_params=request_params)
            elif error_code == 9:
                raise ActionLimitError(error_msg=error_msg, request_params=request_params)
            elif error_code == 10:
                raise InternalServerError(error_msg=error_msg, request_params=request_params)
            elif error_code == 11:
                raise TestAppError(error_msg=error_msg, request_params=request_params)
            elif error_code == 18:
                raise ProfileDeletedError(error_msg=error_msg, request_params=request_params)
            elif error_code == 23:
                raise MethodUnavailableError(error_msg=error_msg, request_params=request_params)
            elif error_code == 30:
                raise PrivateProfileError(error_msg=error_msg, request_params=request_params)
            elif error_code == 203:
                raise GroupAccessError(error_msg=error_msg, request_params=request_params)
            else:
                raise ViKoAPIResponseError(error_code=error_code, error_msg=error_msg,
                                           request_params=request_params)
        if "response" in response:
            data = response["response"]

            # if isinstance(data, list):
            #     return [self._convert_object(method, item) for item in data]
            # else:
            #     return self._convert_object(method, data)
            return self._convert_object(method, data)
        return response

    def _convert_object(self, method: str, data: json):
        """
            Определяет, в какой объект конвертировать JSON-ответ, основываясь на методе API.
        """
        if method == "status.get":
            return data["text"]
        elif method == "users.get":
            pass
        return data
