from datetime import datetime


class WikiPage:
    def __init__(self, page_id: int, group_id: int, creator_id: int, title: str,
                 can_edit: bool, can_edit_access: bool, who_can_view: int,
                 who_can_edit: int, created_unix: int, edited_unix: int,
                 editor_id: int, views: int, parent: str | None, parent2: str | None,
                 source: str | None, html: str | None, view_url: str):
        self.id = page_id
        self.group_id = group_id
        self.creator_id = creator_id
        self.title = title
        self.can_edit = can_edit
        self.can_edit_access = can_edit_access
        self.who_can_view = who_can_view
        self.who_can_edit = who_can_edit
        self.created_datetime = datetime.fromtimestamp(created_unix)
        self.edited_datetime = datetime.fromtimestamp(edited_unix)
        self.editor_id = editor_id
        self.views = views
        self.parent = parent
        self.parent2 = parent2
        self.source = source
        self.html = html
        self.view_url = view_url

    def to_dict(self) -> dict:
        """Returns the wiki page object as a dictionary."""
        return {
            "id": self.id,
            "group_id": self.group_id,
            "creator_id": self.creator_id,
            "title": self.title,
            "current_user_can_edit": self.can_edit,
            "current_user_can_edit_access": self.can_edit_access,
            "who_can_view": self.who_can_view,
            "who_can_edit": self.who_can_edit,
            "created": self.created_datetime.isoformat(),
            "edited": self.edited_datetime.isoformat(),
            "editor_id": self.editor_id,
            "views": self.views,
            "parent": self.parent,
            "parent2": self.parent2,
            "source": self.source,
            "html": self.html,
            "view_url": self.view_url
        }
