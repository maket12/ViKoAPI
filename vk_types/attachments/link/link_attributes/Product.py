from vk_types.price.Price import Price


class LinksProduct:
    def __init__(self, price: Price):
        self.price = price

    def to_dict(self) -> dict:
        """Returns the product object as a dictionary."""
        return {
            "price": self.price.to_dict()
        }
