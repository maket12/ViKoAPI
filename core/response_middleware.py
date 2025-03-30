import json
from core.object_factory import ObjectFactory
from errors.exceptions import *  # maybe replace and do 2 files with exceptions: response's and before response


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
                    raise ApiAppOff(error_msg=error_msg, request_params=request_params)
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
                    raise ProfileDeleted(error_msg=error_msg, request_params=request_params)
                case 19:
                    raise ContentBlocked(error_msg=error_msg, request_params=request_params)
                case 23:
                    raise MethodUnavailable(error_msg=error_msg, request_params=request_params)
                case 30:
                    raise PrivateProfileError(error_msg=error_msg, request_params=request_params)
                case 171:
                    raise InvalidListId(error_msg=error_msg, request_params=request_params)
                case 173:
                    raise MaximumListNumber(error_msg=error_msg, request_params=request_params)
                case 174:
                    raise CannotAddYourself(error_msg=error_msg, request_params=request_params)
                case 175:
                    raise BlacklistedError(error_msg=error_msg, request_params=request_params)
                case 176:
                    raise UserBlacklistedError(error_msg=error_msg, request_params=request_params)
                case 177:
                    raise UserNotFound(error_msg=error_msg, request_params=request_params)
                case 203:
                    raise GroupAccessError(error_msg=error_msg, request_params=request_params)
                case 242:
                    raise TooManyFriends(error_msg=error_msg, request_params=request_params)
                case 3102:
                    raise SpecifiedLinkIncorrect(error_msg=error_msg, request_params=request_params)
                case _:
                    raise ViKoAPIResponseError(error_code=error_code, error_msg=error_msg,
                                               request_params=request_params)
        if "response" in response:
            data = response["response"]

            return self._convert_object(method, data)
        return response

    def _convert_object(self, method: str, data: json):
        parts = method.split('.')
        first_part = parts[0]
        second_part = parts[1]

        if first_part == "status":
            return data["text"]

        elif first_part == "gifts":
            if second_part == "get":
                return self.object_factory.create_gift_items(data.get("items"))
            else:
                return data

        elif first_part == "users":
            match second_part:
                case "get" | "search" | "getFollowers":
                    return self.object_factory.create_users(data.get("items"))
                case "getSubscriptions":
                    return self.object_factory.create_subscriptions(data.get("items"))
                case _:
                    return data

        elif first_part == "friends":
            match second_part:
                case "add":
                    return int(data)
                case "addList":
                    return data["list_id"]
                case "getLists":
                    return self.object_factory.create_friend_lists(data.get("items"))
                case "getOnline":
                    return self.object_factory.create_online_friends(data)
                case "getRecent":
                    return data
                case "areFriends":
                    return self.object_factory.create_friendships(data)
                case "deleteAllRequests":
                    return
                case "getMutual":
                    return self.object_factory.create_mutual_friends(data)
                case "getRequests":
                    return self.object_factory.create_friend_requests(data.get("items"))
                case "getSuggestions":
                    return self.object_factory.create_users(data.get("items"))
                case "search":
                    return self.object_factory.create_users(data.get("items"))
                case _:
                    return data

        elif first_part == "likes":
            match second_part:
                case "add" | "delete":
                    return self.object_factory.create_reactions(data.get("items"))
                case "getList":
                    return self.object_factory.create_likes_list(data.get("items"))
                case "isLiked":
                    return bool(data.get("liked")), bool(data.get("copied"))

        elif first_part == "groups":
            match second_part:
                case "search":
                    return
                case _:
                    return data

        elif first_part == "wall":
            match second_part:
                case "get":
                    return self.object_factory.create_posts(data.get("items"))
                case "wall.checkCopyrightLink" | "wall.closeComments":
                    return True
                case _:
                    return data

        else:
            return data
