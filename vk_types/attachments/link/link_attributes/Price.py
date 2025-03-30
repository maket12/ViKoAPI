from vk_types.attachments.link.link_attributes.Currency import PricesCurrency


class ProductsPrice:
    def __init__(self, amount: int, currency: PricesCurrency, text: str):
        self.amount = amount / 100
        self.currency = currency
        self.text = text

    def to_dict(self) -> dict:
        """Returns the product price object as a dictionary."""
        return {
            "amount": self.amount * 100,
            "currency": self.currency.to_dict(),
            "text": self.text
        }
