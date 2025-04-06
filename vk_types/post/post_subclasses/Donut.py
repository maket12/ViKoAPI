from enums.post.donut_edit_mode import DonutsEditMode


class PostsDonut:
    def __init__(self, is_donut: bool, paid_duration: int, placeholder: object | None,
                 can_publish_free_copy: bool, edit_mode: DonutsEditMode | None):
        self.is_donut = is_donut
        self.paid_duration = paid_duration
        self.placeholder = placeholder
        self.can_publish_free_copy = can_publish_free_copy
        self.edit_mode = edit_mode

    def to_dict(self) -> dict:
        return {
            "is_donut": self.is_donut,
            "paid_duration": self.paid_duration,
            "placeholder": self.placeholder,
            "can_publish_free_copy": self.can_publish_free_copy,
            "edit_mode": self.edit_mode.value if self.edit_mode else None
        }

