from vk_types.album.Album import Album
from core.object_factory.attachments_factory import AttachmentsFactory


class AlbumsFactory:
    @staticmethod
    def create_album(data: dict) -> Album:
        mapped_data = {
            "album_id": data.get("id"),
            "thumb_id": data.get("thumb_id"),
            "owner_id": data.get("owner_id"),
            "title": data.get("title"),
            "description": data.get("description"),
            "created_unix": data.get("created"),
            "updated_unix": data.get("updated"),
            "size": data.get("size"),
            "can_upload": bool(data.get("can_upload")),
            "photo_sizes": AttachmentsFactory.create_photos(data.get("photo_sizes")) if data.get("photo_sizes") else None,
        }
        return Album(**mapped_data)

    @staticmethod
    def create_albums(items: list) -> list[Album]:
        return [AlbumsFactory.create_album(item) for item in items]
