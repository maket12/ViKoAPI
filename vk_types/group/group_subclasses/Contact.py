class GroupContact:
    def __init__(self, user_id: int, desc: str, phone: str, email: str):
        self.user_id = user_id
        self.desc = desc
        self.phone = phone
        self.email = email

    def to_dict(self) -> dict:
        """Returns the group contact object as a dictionary."""
        return {
            "user_id": self.user_id,
            "desc": self.desc,
            "phone": self.phone,
            "email": self.email
        }
