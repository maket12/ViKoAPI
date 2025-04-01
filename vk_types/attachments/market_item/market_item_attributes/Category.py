from vk_types.attachments.market_item.market_item_attributes.Section import CategorySection


class MarketItemCategory:
    def __init__(self, category_id: int, name: str, section: CategorySection):
        self.id = category_id
        self.name = name
        self.section = section

    def to_dict(self) -> dict:
        """Returns the market item category object as a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "section": self.section.to_dict()
        }
