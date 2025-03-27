class Sticker:
    def __init__(self, sticker_id: int, product_id: int, is_allowed: bool, inner_type: str):
        self.id = sticker_id
        self.product_id = product_id
        self.is_allowed = is_allowed
        self.inner_type = inner_type

    def to_dict(self) -> dict:
        """Returns the photo object as a dictionary."""
        return {
            "sticker_id": self.id,
            "product_id": self.product_id,
            "is_allowed": self.is_allowed,
            "inner_type": self.inner_type
        }
