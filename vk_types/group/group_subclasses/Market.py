from enums.group.market_type import MarketType
from vk_types.price.prices_subclasses.Currency import PricesCurrency


class GroupMarket:
    def __init__(self, is_enabled: bool, market_type: MarketType | None, price_min: int | None,
                 price_max: int | None, main_album_id: int | None, contact_id: int | None,
                 currency: PricesCurrency | None, currency_text: str | None):
        self.is_enabled = is_enabled
        self.type = market_type
        self.price_min = price_min
        self.price_max = price_max
        self.main_album_id = main_album_id
        self.contact_id = contact_id
        self.currency = currency
        self.currency_text = currency_text

    def to_dict(self) -> dict:
        """Returns the group market object as a dictionary."""
        return {
            "enabled": self.is_enabled,
            "type": self.type.value if self.type is not None else None,
            "price_min": self.price_min,
            "price_max": self.price_max,
            "main_album_id": self.main_album_id,
            "contact_id": self.contact_id,
            "currency": self.currency.to_dict(),
            "currency_text": self.currency_text
        }
