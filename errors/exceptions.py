class ViKoAPIError(Exception):
    def __init__(self, error_msg: str):
        super().__init__(f"{error_msg}")


class ClientParamsEmpty(ViKoAPIError):
    def __init__(self):
        super().__init__("You can't create client object without any parameter.")


class InvalidCountError(ViKoAPIError):
    """
    For methods wall.get and wall.getComments
    """
    def __init__(self, count: int, max_count: int):
        super().__init__(f"Invalid count value: {count}. Maximum allowed is {max_count}")
        self.count = count
        self.max_count = max_count


class NegativeValueError(ViKoAPIError):
    def __init__(self, parameter_name: str, value: any):
        super().__init__(f"{parameter_name.capitalize()} value cannot be negative: {value}.")
        self.parameter = parameter_name
        self.value = value


class InvalidUserID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid user_id: {value}.")
        self.value = value


class InvalidGroupID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid group_id: {value}.")
        self.value = value


class InvalidPostID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid post_id: {value}.")
        self.value = value


class InvalidCommentID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid comment_id: {value}.")
        self.value = value


class InvalidStickerID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid sticker_id: {value}.")
        self.value = value


class InvalidPhotoID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid photo_id: {value}.")
        self.value = value


class InvalidTagID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid tag_id: {value}.")
        self.value = value


class InvalidAlbumID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid album_id: {value}.")
        self.value = value


class InvalidFileID(ViKoAPIError):
    def __init__(self, value: int):
        super().__init__(f"Invalid file_id: {value}.")
        self.value = value


class UndefinedParameterValue(ViKoAPIError):
    def __init__(self, parameter_name: str, value: any):
        super().__init__(f"Parameter {parameter_name} cannot be {value}.")
        self.parameter = parameter_name
        self.value = value


class AmountLimit(ViKoAPIError):
    def __init__(self, parameter_name: str, limit: int):
        super().__init__(f"Amount of {parameter_name} cannot be greater than {limit}.")
        self.parameter = parameter_name
        self.limit = limit


class TooLongText(ViKoAPIError):
    def __init__(self, text_length: int):
        super().__init__(f"Length of the text cannot be greater than 500 symbols.")
        self.text_length = text_length


class ViKoAPIResponseError(ViKoAPIError):
    """
    Errors from responses.
    """
    def __init__(self, code: int, msg: str, request_params: dict = None):
        super().__init__(f"{msg}")
        self.code = code
        self.msg = msg
        self.request_params = request_params or {}


class UnknownError(ViKoAPIResponseError):
    """Unknown error occurred. Try again later!"""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(1, msg, request_params)


class AuthorisationError(ViKoAPIResponseError):
    """Check your token or authorisation schema"""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(5, msg,
                         request_params)


class RateLimitError(ViKoAPIResponseError):
    """Too many requests per second."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(6, msg, request_params)


class ProfileDeleted(ViKoAPIResponseError):
    """User was deleted or blocked"""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(18, msg, request_params)


class ApiAppOff(ViKoAPIResponseError):
    """Check your api access app is not off"""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(2, msg, request_params)


class ActionLimitError(ViKoAPIResponseError):
    """Too many same actions"""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(9, msg, request_params)


class InternalServerError(ViKoAPIResponseError):
    """Server returned error because of internal reasons."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(10, msg, request_params)


class TestAppError(ViKoAPIResponseError):
    """Test API access app must be off or user must be logged in."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(11, msg, request_params)


class ContentBlocked(ViKoAPIResponseError):
    """Perhaps the group or user was blocked."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(19, msg, request_params)


class MethodUnavailable(ViKoAPIResponseError):
    """This method is unavailable for this moment"""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(23, msg, request_params)


class PrivateProfileError(ViKoAPIResponseError):
    """Cannot get data from private profile"""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(30, msg, request_params)


class GroupAccessError(ViKoAPIResponseError):
    """Cannot get access to this group(you're not a member or an administrator"""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(203, msg, request_params)


class NotFound(ViKoAPIResponseError):
    """Wall's post or comment was not found."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(104, msg, request_params)


class InvalidListId(ViKoAPIResponseError):
    """Invalid list id."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(171, msg, request_params)


class MaximumListNumber(ViKoAPIResponseError):
    """Reached the maximum number of lists."""

    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(173, msg, request_params)


class CannotAddYourself(ViKoAPIResponseError):
    """Cannot add yourself as friend."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(174, msg, request_params)


class BlacklistedError(ViKoAPIResponseError):
    """Cannot add this user to friends as they have put you on their blacklist."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(175, msg, request_params)


class UserBlacklistedError(ViKoAPIResponseError):
    """Cannot add this user to friends as you put him on blacklist."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(176, msg, request_params)


class UserNotFound(ViKoAPIResponseError):
    """Cannot add this user to friends as user not found."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(177, msg, request_params)


class WallPostAccessError(ViKoAPIResponseError):
    """Access to wall's post denied."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(210, msg, request_params)


class WallCommentAccessError(ViKoAPIResponseError):
    """Access to wall's comment denied."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(211, msg, request_params)


class PostCommentsAccessError(ViKoAPIResponseError):
    """Access to post comments denied."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(212, msg, request_params)


class StatusRepliesAccessError(ViKoAPIResponseError):
    """Access to status replies denied."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(213, msg, request_params)


class AddingPostAccessError(ViKoAPIResponseError):
    """Access to adding post denied."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(214, msg, request_params)


class TooManyRecipients(ViKoAPIResponseError):
    """Too many recipients."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(220, msg, request_params)


class HyperlinksForbidden(ViKoAPIResponseError):
    """Hyperlinks are forbidden."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(222, msg, request_params)


class TooManyReplies(ViKoAPIResponseError):
    """Too many replies."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(223, msg, request_params)


class TooManyAdsPosts(ViKoAPIResponseError):
    """Too many ads posts."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(224, msg, request_params)


class DonutDisabled(ViKoAPIResponseError):
    """Donut is disabled."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(225, msg, request_params)


class TooManyFriends(ViKoAPIResponseError):
    """Too many friends."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(242, msg, request_params)


class CommentNotDeleted(ViKoAPIResponseError):
    """Comment has not been deleted."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(243, msg, request_params)


class Disabled2FA(ViKoAPIResponseError):
    """You need to enable 2FA for this action."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(703, msg, request_params)


class InvalidDocumentTitle(ViKoAPIResponseError):
    """Invalid document title."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(1152, msg, request_params)


class AccessDocumentDenied(ViKoAPIResponseError):
    """Access to document is denied."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(1153, msg, request_params)


class SpecifiedLinkIncorrect(ViKoAPIResponseError):
    """Specified link is incorrect (can't find source)."""
    def __init__(self, msg: str, request_params: dict = None):
        super().__init__(3102, msg, request_params)
