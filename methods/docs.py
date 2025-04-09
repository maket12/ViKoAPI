from typing import Coroutine, Any, Tuple
from core.session_mixin import SessionMixin
from enums.attachments.file.file_type import FileType
from vk_types.attachments.file.File import File
from errors.exceptions import *


class DocsMethods(SessionMixin):
    def copy(self, owner_id: int, file_id: int,
             access_key: str | None = None) -> Coroutine[Any, Any, int]:
        if file_id <= 0:
            raise InvalidFileID(file_id)

        params = {"owner_id": owner_id, "doc_id": file_id}

        if access_key:
            params["access_key"] = access_key

        return self.request_async("docs.add", params)

    def delete(self, file_id: int, owner_id: int | None = None) -> Coroutine[Any, Any, None]:
        if file_id <= 0:
            raise InvalidFileID(file_id)

        params = {}

        if owner_id:
            params["owner_id"] = owner_id
        params["doc_id"] = file_id

        return self.request_async("docs.delete", params)

    def edit(self, file_id: int, title: str, owner_id: int | None = None,
             tags: str | None = None) -> Coroutine[Any, Any, None]:
        if file_id <= 0:
            raise InvalidFileID(file_id)

        params = {"title": title}

        if owner_id:
            params["owner_id"] = owner_id

        params["doc_id"] = file_id

        if tags:
            params["tags"] = tags

        return self.request_async("docs.edit", params)

    def get(self, owner_id: int | None = None, count: int | None = None,
            offset: int | None = None, file_type: FileType | int | None = None,
            return_tags: bool = False) -> Coroutine[Any, Any, list[File]]:
        params = {}

        if owner_id:
            params["owner_id"] = owner_id
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if file_type:
            if isinstance(file_type, int):
                params["file_type"] = file_type
            else:
                params["file_type"] = file_type.value
        params["return_tags"] = int(return_tags)

        return self.request_async("docs.get", params)

    def get_by_id(self, file_links: list[Tuple[int, int]],
                  return_tags: bool = False) -> Coroutine[Any, Any, list[File]]:
        """
        :param file_links: represents a file link in format <OWNER_ID>_<FILE_ID>
        :param return_tags: do the tags need to return
        :return: list of File objects
        """
        params = {"docs": ','.join(f"{parts[0]}_{parts[1]}" for parts in file_links),
                  "return_tags": int(return_tags)}
        return self.request_async("docs.get", params)

    def get_types(self, owner_id: int | None = None):
        params = {}

        if owner_id:
            params["owner_id"] = owner_id

        return self.request_async("docs.getTypes", params)

    def search(self, q: str, count: int | None = None,
               offset: int | None = None, search_own: bool = False,
               return_tags: bool = False) -> Coroutine[Any, Any, list[File]]:
        params = {"q": q}

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        params["search_own"] = int(search_own)
        params["return_tags"] = int(return_tags)

        return self.request_async("docs.search", params)
