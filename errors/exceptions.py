class ViKoAPIError(Exception):
    pass


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


class ViKoAPIResponseError(ViKoAPIError):
    """
    Errors from responses.
    """
    def __init__(self, error_code: int, error_msg: str, request_params: dict = None):
        super().__init__(f"{error_msg}")
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_params = request_params or {}


class UnknownError(ViKoAPIResponseError):
    """Unknown error occurred. Try again later!"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(1, error_msg, request_params)


class AuthorisationError(ViKoAPIResponseError):
    """Check your token or authorisation schema"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(5, error_msg,
                         request_params)


class RateLimitError(ViKoAPIResponseError):
    """Too many requests per second."""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(6, error_msg, request_params)


class ProfileDeletedError(ViKoAPIResponseError):
    """User was deleted or blocked"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(18, error_msg, request_params)


class ApiAppOffError(ViKoAPIResponseError):
    """Check your api access app is not off"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(2, error_msg, request_params)


class ActionLimitError(ViKoAPIResponseError):
    """Too many same actions"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(9, error_msg, request_params)


class InternalServerError(ViKoAPIResponseError):
    """Server returned error because of internal reasons"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(10, error_msg, request_params)


class TestAppError(ViKoAPIResponseError):
    """Test API access app must be off or user must be logged in"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(11, error_msg, request_params)


class MethodUnavailableError(ViKoAPIResponseError):
    """This method is unavailable for this moment"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(23, error_msg, request_params)


class PrivateProfileError(ViKoAPIResponseError):
    """Cannot get data from private profile"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(30, error_msg, request_params)


class GroupAccessError(ViKoAPIResponseError):
    """Cannot get access to this group(you're not a member or an administrator"""
    def __init__(self, error_msg: str, request_params: dict = None):
        super().__init__(203, error_msg, request_params)
