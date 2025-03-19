class Gift:
    def __init__(self, gift_id: int, thumb_256: str | None, thumb_96: str | None,
                 thumb_48: str | None):
        self.gift_id = gift_id
        self.thumb_256 = thumb_256
        self.thumb_96 = thumb_96
        self.thumb_48 = thumb_48

