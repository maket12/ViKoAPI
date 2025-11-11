class UsersContacts:
    def __init__(self, mobile_phone: str | None, home_phone: str | None):
        """
        Represents user.contact object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param mobile_phone: Mobile phone
        :param home_phone: Home phone (if available)
        """
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone

    def to_dict(self) -> dict:
        return {
            "mobile_phone": self.mobile_phone,
            "hope_phone": self.home_phone
        }
