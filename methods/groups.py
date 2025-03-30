from typing import Union, Coroutine, Any
from core.session_mixin import SessionMixin
from enums.group.fields import GroupFields
from errors.exceptions import *


class GroupsMethods(SessionMixin):
    def get_by_id(self, group_ids: list, fields: list[GroupFields] | str = None):
        params = {}
        groups_length = len(group_ids)
        if groups_length == 0:
            raise UndefinedParameterValue("group_ids", group_ids)
        if groups_length > 500:
            raise AmountLimit("groups_ids", 500)

        if groups_length == 1:
            params["group_id"] = group_ids[0]
        else:
            params["group_ids"] = ','.join(group_ids)

        if fields:
            params["fields"] = ','.join(fields)

        return self.request_async("groups.getById", params)

    def search_groups(self, text: str, group_type: str = None, country_id: int = None,
                      city_id: int = None, future: bool = False,
                      market: bool = False, sort: bool = False,
                      offset: int = None, count: int = 100):
        params = {"q": text}

        if group_type:
            params["type"] = group_type
        if country_id:
            params["country_id"] = country_id
        if city_id:
            params["city_id"] = city_id
        if future:
            params["future"] = future
        if market:
            params["market"] = market
        if sort:
            params["sort"] = 6
        if offset:
            params["offset"] = offset
        if count:
            if count > 1000:
                raise InvalidCountError(count, 1000)
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        return self.request_async("groups.search", params)
