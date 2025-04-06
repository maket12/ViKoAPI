from datetime import datetime
from enums.attachments.market_item.market_item_availability import MarketItemAvailability
from vk_types.price.Price import Price
from vk_types.attachments.market_item.market_item_attributes.Dimensions import MarketItemDimensions
from vk_types.attachments.market_item.market_item_attributes.Category import MarketItemCategory
from vk_types.attachments.market_item.market_item_attributes.RejectInfo import MarketRejectInfo
from vk_types.attachments.photo.Photo import Photo


class MarketItem:
    def __init__(self, item_id: int, owner_id: int, title: str, description: str,
                 price: Price, dimensions: MarketItemDimensions | None, weight: int,
                 category: MarketItemCategory, thumb_photo: str, date_unix: int,
                 availability: MarketItemAvailability, is_favorite: bool, sku: str,
                 reject_info: MarketRejectInfo, photos: list[Photo] | None,
                 can_comment: bool | None, can_repost: bool | None,
                 likes: int | None, is_liked: bool | None,
                 url: str | None, button_title: str | None):
        self.id = item_id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.price = price
        self.dimensions = dimensions
        self.weight = weight
        self.category = category
        self.thumb_photo = thumb_photo
        self.datetime = datetime.fromtimestamp(date_unix)
        self.availability = availability
        self.is_favorite = is_favorite
        self.sku = sku
        self.reject_info = reject_info
        self.photos = photos
        self.can_comment = can_comment
        self.can_repost = can_repost
        self.likes = likes
        self.is_liked = is_liked
        self.url = url
        self.button_title = button_title

    def to_dict(self) -> dict:
        """Returns the market item object as a dictionary."""
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "title": self.title,
            "description": self.description,
            "price": self.price.to_dict(),
            "dimensions": self.dimensions.to_dict(),
            "weight": self.weight,
            "category": self.category.to_dict(),
            "thumb_photo": self.thumb_photo,
            "date": datetime.isoformat(self.datetime),
            "availability": self.availability.value,
            "is_favorite": self.is_favorite,
            "sku": self.sku,
            "reject_info": self.reject_info.to_dict(),
            "photos": [photo.to_dict() for photo in self.photos],
            "can_comment": int(self.can_comment),
            "can_repost": int(self.can_repost),
            "likes": {
                "user_likes": self.is_liked,
                "count": self.likes
            },
            "url": self.url,
            "button_title": self.button_title
        }
