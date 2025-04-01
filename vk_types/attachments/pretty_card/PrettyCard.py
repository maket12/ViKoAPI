from vk_types.attachments.photo.Photo import Photo
from vk_types.button.Button import Button


class PrettyCard:
    def __init__(self, card_id: int, link_url: str, title: str, photos: list[Photo],
                 button: Button | None, price: str, old_price: str):
        self.id = card_id
        self.url = link_url
        self.title = title
        self.photos = photos
        self.button = button
        self.price = price
        self.old_price = old_price

    def to_dict(self) -> dict:
        """Returns the pretty card object as a dictionary."""
        return {
            "card_id": self.id,
            "link_url": self.url,
            "title": self.title,
            "images": [photo.to_dict() for photo in self.photos],
            "button": self.button.to_dict() if self.button else None,
            "price": self.price,
            "price_old": self.old_price
        }
