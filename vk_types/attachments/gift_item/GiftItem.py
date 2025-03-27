from datetime import datetime
from vk_types.attachments.gift_item.gift_item_attributes.Gift import Gift


class GiftItem:
    def __init__(self, gift_item_id: int, from_user_id: int | None, message: str | None, unix_date: int,
                 gift: Gift, privacy: int):
        self.gift_item_id = gift_item_id
        self.from_user_id = from_user_id
        self.message = message
        self.datetime = datetime.fromtimestamp(unix_date)
        self.gift = gift
        self.privacy = privacy
