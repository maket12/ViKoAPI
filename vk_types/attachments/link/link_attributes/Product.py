from vk_types.attachments.link.link_attributes.Price import ProductsPrice


class LinksProduct:
    def __init__(self, price: ProductsPrice):
        self.price = price

    def to_dict(self) -> dict:
        """Returns the product object as a dictionary."""
        return {
            "price": self.price.to_dict()
        }
