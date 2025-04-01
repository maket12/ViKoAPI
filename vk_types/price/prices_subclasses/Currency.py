class PricesCurrency:
    def __init__(self, currency_id: int, name: str):
        self.id = currency_id
        self.name = name

    def to_dict(self) -> dict:
        """Returns the price currency object as a dictionary."""
        return {
            "id": self.id,
            "name": self.name
        }
