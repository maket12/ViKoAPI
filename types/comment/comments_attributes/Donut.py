class CommentsDonut:
    def __init__(self, is_don: bool, placeholder: str | None):
        self.is_don = is_don
        self.placeholder = placeholder

    def to_dict(self) -> dict:
        """Returns the Donut as a dictionary."""
        return {
            "is_don": self.is_don,
            "placeholder": self.placeholder
        }
