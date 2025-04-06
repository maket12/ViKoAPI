from vk_types.attachments.photo.Photo import Photo
from vk_types.price.Price import Price
from vk_types.button.Button import Button


class Link:
    def __init__(self, url: str, title: str, caption: str, description: str, photo: Photo | None,
                 price: Price | None, button: Button | None,
                 preview_page: str, preview_url: str):
        self.url = url
        self.title = title
        self.caption = caption
        self.description = description
        self.photo = photo
        self.product = price
        self.button = button
        self.preview_page = preview_page
        self.preview_url = preview_url

    def to_dict(self) -> dict:
        """Returns the link object as a dictionary."""
        return {
            "url": self.url,
            "title": self.title,
            "caption": self.caption,
            "description": self.description,
            "photo": self.photo.to_dict(),
            "product": {
                "price": self.product.to_dict()
            },
            "button": self.button.to_dict(),
            "preview_page": self.preview_page,
            "preview_url": self.preview_url
        }
