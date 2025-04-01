from enums.post.donut_edit_mode import DonutsEditMode


class PostsDonut:
    def __init__(self, is_donut: bool, paid_duration: int, placeholder: object | None,
                 can_publish_free_copy: bool, edit_mode: DonutsEditMode | str):
        self.is_donut = is_donut
        self.paid_duration = paid_duration
        self.placeholder = placeholder
        self.can_publish_free_copy = can_publish_free_copy
        self.edit_mode = edit_mode
