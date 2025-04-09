import json
from core.object_factory.object_factory import ObjectFactory
from errors.exceptions import *  # maybe replace and do 2 files with exceptions: response's and before response


class ResponseMiddleware:
    """
       Middleware for processing API responses and automatically converting JSON into objects.
    """

    def __init__(self, object_factory: ObjectFactory):
        self.object_factory = object_factory

    def process(self, method: str, response: dict):
        """
            Processes the API response, automatically converting to objects if the method is supported.
        """
        if "error" in response:
            error = response["error"]
            error_code = error.get("error_code")
            error_msg = error.get("error_msg")
            request_params = error.get("request_params")

            match error_code:
                case 1:
                    raise UnknownError(error_msg, request_params)
                case 2:
                    raise ApiAppOff(error_msg, request_params)
                case 5:
                    raise AuthorisationError(error_msg, request_params)
                case 6:
                    raise RateLimitError(error_msg, request_params)
                case 9:
                    raise ActionLimitError(error_msg, request_params)
                case 10:
                    raise InternalServerError(error_msg, request_params)
                case 11:
                    raise TestAppError(error_msg, request_params)
                case 18:
                    raise ProfileDeleted(error_msg, request_params)
                case 19:
                    raise ContentBlocked(error_msg, request_params)
                case 23:
                    raise MethodUnavailable(error_msg, request_params)
                case 30:
                    raise PrivateProfileError(error_msg, request_params)
                case 104:
                    raise NotFound(error_msg, request_params)
                case 171:
                    raise InvalidListId(error_msg, request_params)
                case 173:
                    raise MaximumListNumber(error_msg, request_params)
                case 174:
                    raise CannotAddYourself(error_msg, request_params)
                case 175:
                    raise BlacklistedError(error_msg, request_params)
                case 176:
                    raise UserBlacklistedError(error_msg, request_params)
                case 177:
                    raise UserNotFound(error_msg, request_params)
                case 203:
                    raise GroupAccessError(error_msg, request_params)
                case 210:
                    raise WallPostAccessError(error_msg, request_params)
                case 211:
                    raise WallCommentAccessError(error_msg, request_params)
                case 212:
                    raise PostCommentsAccessError(error_msg, request_params)
                case 213:
                    raise StatusRepliesAccessError(error_msg, request_params)
                case 214:
                    raise AddingPostAccessError(error_msg, request_params)
                case 220:
                    raise TooManyRecipients(error_msg, request_params)
                case 222:
                    raise HyperlinksForbidden(error_msg, request_params)
                case 223:
                    raise TooManyReplies(error_msg, request_params)
                case 224:
                    raise TooManyAdsPosts(error_msg, request_params)
                case 225:
                    raise DonutDisabled(error_msg, request_params)
                case 242:
                    raise TooManyFriends(error_msg, request_params)
                case 243:
                    raise CommentNotDeleted(error_msg, request_params)
                case 703:
                    raise Disabled2FA(error_msg, request_params)
                case 1152:
                    raise InvalidDocumentTitle(error_msg, request_params)
                case 1153:
                    raise AccessDocumentDenied(error_msg, request_params)
                case 3102:
                    raise SpecifiedLinkIncorrect(error_msg, request_params)
                case _:
                    raise ViKoAPIResponseError(error_code, error_msg, request_params)

        if "response" in response:
            data = response["response"]
            return self._convert_object(method, data)

        return response

    def _convert_object(self, method: str, data):
        parts = method.split('.')
        first_part = parts[0]
        second_part = parts[1]

        if first_part == "status":
            return data["text"]

        elif first_part == "gifts":
            if second_part == "get":
                return self.object_factory.attachments.create_gift_items(data.get("items"))
            else:
                return data

        elif first_part == "users":
            match second_part:
                case "get" | "search" | "getFollowers":
                    return self.object_factory.user.create_users(data.get("items"))
                case "getSubscriptions":
                    return self.object_factory.friends.create_subscriptions(data.get("items"))
                case _:
                    return data

        elif first_part == "friends":
            match second_part:
                case "add":
                    return int(data)
                case "addList":
                    return data["list_id"]
                case "getLists":
                    return self.object_factory.friends.create_friend_lists(data.get("items"))
                case "getOnline":
                    return self.object_factory.friends.create_online_friends(data)
                case "getRecent":
                    return data
                case "areFriends":
                    return self.object_factory.friends.create_friendships(data)
                case "deleteAllRequests":
                    return
                case "getMutual":
                    return self.object_factory.friends.create_mutual_friends(data)
                case "getRequests":
                    return self.object_factory.friends.create_friend_requests(data.get("items"))
                case "getSuggestions":
                    return self.object_factory.user.create_users(data.get("items"))
                case "search":
                    return self.object_factory.user.create_users(data.get("items"))
                case _:
                    return data

        elif first_part == "likes":
            match second_part:
                case "add" | "delete":
                    return self.object_factory.likes.create_reactions(data.get("items"))
                case "getList":
                    return self.object_factory.likes.create_likes_list(data.get("items"))
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
                case "get" | "getById" | "getReposts" | "search":
                    if data.get("profiles") or data.get("groups"):
                        return (
                            self.object_factory.post.create_posts(data.get("items")),
                            self.object_factory.user.create_users(data.get("profiles")) if data.get("profiles") else None,
                            self.object_factory.groups.create_groups(data.get("groups")) if data.get("groups") else None
                        )
                    return self.object_factory.post.create_posts(data.get("items"))
                # case "getComment":
                #     return self.object_factory.comments.create_comment(data.get())
                case "getComments":
                    if data.get("profiles") or data.get("groups"):
                        return (
                            self.object_factory.comments.create_comments(data.get("items")),
                            self.object_factory.user.create_users(data.get("profiles")) if data.get("profiles") else None,
                            self.object_factory.groups.create_groups(data.get("groups")) if data.get("groups") else None
                        )
                    return self.object_factory.comments.create_comments(data.get("items"))
                case "wall.checkCopyrightLink" | "wall.closeComments":
                    return True
                case ("pin" | "unpin" | "reportPost" | "reportComment" | "restore" | "restoreComment" | "openComments" |
                      "editComment" | "delete" | "deleteComment"):
                    return
                case "repost" | "post" | "edit":
                    return data.get("post_id")
                case "createComment":
                    return data.get("comment_id"), data.get("parent_stack")
                case _:
                    return data

        elif first_part == "photos":
            match second_part:
                case "search":
                    return self.object_factory.attachments.create_photos(data.get("items"))
                case "deleteComment":
                    return bool(int(data))
                case "confirmTag" | "delete" | "deleteAlbum":
                    return
                case _:
                    return data

        elif first_part == "docs":
            match second_part:
                case "get" | "get_by_id" | "search":
                    return self.object_factory.attachments.create_files(data.get("items"))
                case "getTypes":
                    return self.object_factory.attachments.create_file_types(data.get("items"))
                case "add":
                    return data
                case "delete" | "edit":
                    return
                case _:
                    return data


        else:
            return data
