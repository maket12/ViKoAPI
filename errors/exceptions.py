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
