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
        elif method == "gifts.get":
            return self.object_factory.create_gift_items(data.get("items"))
        return data

# test = {
#     "response": {
#         "count": 129,
#         "items": [
#             {
#                 "date": 1707893847,
#                 "from_id": 0,
#                 "gift": {
#                     "id": 845,
#                     "thumb_512": "https://vk.com/images/gift/845/512.png",
#                     "thumb_256": "https://vk.com/images/gift/845/256.png",
#                     "thumb_48": "https://vk.com/images/gift/845/48.png",
#                     "thumb_96": "https://vk.com/images/gift/845/96.png"
#                 },
#                 "gift_hash": "Jvx20l0bq1PPS2Possv8onN87lf5tTi90oPRPGj0MrLjAsyKc5ki5F90BKUdzC8f5T1xtdM/RcWw36u1qr9E//2dVOkusvay*nLDYH6evKDpSWhVGEApvZYE8ArmpSsT1p0GET*P2YoQ5QU6iJMV6e9fj7GRvvAh/xRP49DRXTw-",
#                 "id": -1483196792,
#                 "message": "ааа, с праздником 🥳",
#                 "privacy": 2
#             },
#             {
#                 "date": 1704042147,
#                 "from_id": 288281347,
#                 "gift": {
#                     "id": 1449,
#                     "thumb_512": "https://vk.com/images/gift/1449/512.png",
#                     "thumb_256": "https://vk.com/images/gift/1449/256.png",
#                     "thumb_48": "https://vk.com/images/gift/1449/48.png",
#                     "thumb_96": "https://vk.com/images/gift/1449/96.png"
#                 },
#                 "gift_hash": "IJBuGHMQkngs8/TvqkRjjIenjk3IY4zBhDBCZ75amSbqABJG*jaNUsPl4SXR3YmHY0u9IAkCCJKDs*30214G*MszXM0QuwtTa7k*VEMjWgNP8nyK0rIC8UKE1ATdSU**Atl1LXTHlpM/l/dQbLww1LAPXZ*yfuGa6JgcfPMCS64-",
#                 "id": 30790661,
#                 "message": "с новым годом)",
#                 "privacy": 0
#             },
#             {
#                 "date": 1704033683,
#                 "from_id": 689519813,
#                 "gift": {
#                     "id": 1449,
#                     "thumb_512": "https://vk.com/images/gift/1449/512.png",
#                     "thumb_256": "https://vk.com/images/gift/1449/256.png",
#                     "thumb_48": "https://vk.com/images/gift/1449/48.png",
#                     "thumb_96": "https://vk.com/images/gift/1449/96.png"
#                 },
#                 "gift_hash": "jPnHqHO0sl/xFNwag8bhGbJYGQyOlr*3*HxAzWJ9xZ52yXsnMV*DX*uzofyfq9w1qs7y/gLJ7/RIVcXKDW9e33Y2S4UhCsgKrodePhUbirNJq/Zh*tMSsqbA9tmJIakwsXjXCwjnivBR1QjzvRie5dkotRAdBUugiUEM1bBJmzU-",
#                 "id": 25462703,
#                 "message": "С наступающим!!🎉🔥",
#                 "privacy": 1
#             }
#         ]
#     }
# }
#
# some = ResponseMiddleware(ObjectFactory())
#
# list = some.process(method="gifts.get", response=test)
# for l in list:
#     print(l.datetime)
