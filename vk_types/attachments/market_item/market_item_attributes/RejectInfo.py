class MarketRejectInfo:
    def __init__(self, title: str, description: str, buttons: object | None,
                 moderation_status: int, info_link: str, white_to_support_link: str):
        self.title = title
        self.description = description
        self.buttons = buttons
        self.moderation_status = moderation_status
        self.info_link = info_link
        self.white_to_support_link = white_to_support_link

    def to_dict(self) -> dict:
        """Returns the market reject info object as a dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "buttons": self.buttons,
            "moderation_status": self.moderation_status,
            "info_link": self.info_link,
            "white_to_support_link": self.white_to_support_link
        }
