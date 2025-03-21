from typing import Union, Coroutine, Any
from core.session_mixin import SessionMixin
from enums.wall.filters import WallFilters
from enums.club.fields import ClubFields
from enums.user.fields import UserFields
from enums.user.sex import Sex
from errors.exceptions import InvalidCountError, NegativeValueError, UndefinedParameterValue, AmountLimit
from vk_types.gift_item.GiftItem import GiftItem


class RawMethod(SessionMixin):
    def method(self, method_name: str, params: dict):
        return self.request_async(method_name, params)


class StatusMethods(SessionMixin):
    def set(self, text: str, group_id: int = None):
        params = {"text": text}
        if group_id:
            if group_id < 0:
                raise NegativeValueError("group_id", group_id)
            params["group_id"] = group_id
        return self.request_async("status.set", params)

    def get(self, user_id: int = None, group_id: int = None) -> Coroutine[Any, Any, str]:
        if user_id:
            params = {"user_id": user_id}
        elif group_id:
            if group_id < 0:
                raise NegativeValueError("group_id", group_id)
            params = {"group_id": group_id}
        else:
            params = {}
        return self.request_async("status.get", params)

    def get_my(self) -> Coroutine[Any, Any, str]:
        params = {}
        return self.request_async("status.get_my", params)


class GroupsMethods(SessionMixin):
    def get_by_id(self, group_ids: list, fields: list[ClubFields] | str = None):
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


class WallMethods(SessionMixin):
    def get(self, owner_id: int = None, domain: str = None,
            offset: int = None, count: int = None,
            wall_filter: WallFilters | str = WallFilters.ALL,
            extended: bool = False,
            fields: Union[list[ClubFields], list[UserFields]] | str = None):
        params = {}
        if owner_id:
            params["owner_id"] = owner_id
        if domain:
            params["domain"] = domain
        if offset:
            params["offset"] = offset
        if count:
            params["count"] = count
        if wall_filter:
            params["filter"] = wall_filter
        if extended:
            params["extended"] = True
            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str

        return self.request_async("wall.get", params)

    def get_comment(self, owner_id: int, comment_id: int, extended: bool = False,
                    fields: Union[list[ClubFields], list[UserFields]] | str = None):
        if comment_id <= 0:
            raise NegativeValueError("comment_id", comment_id)

        params = {"owner_id": owner_id, "comment_id": comment_id}

        if extended:
            params["extended"] = 1
            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str

        return self.request_async("wall.getComment", params)

    def get_comments(self, owner_id: int, post_id: int,
                     need_likes: bool = False, start_comment_id: int = None,
                     offset: int = None, count: int = 10,
                     sort: int = -1, preview_length: int = 0,
                     extended: bool = False, fields: Union[list[ClubFields], list[UserFields]] | str = None,
                     comment_id: int = None, thread_items_count: int = None):
        """
                sort = -1 - desc(from newest to oldest)
                sort = 1 - asc(from oldest to newest)
        """
        params = {"owner_id": owner_id, "post_id": post_id}

        if need_likes:
            params["need_likes"] = 1
        if start_comment_id:
            params["start_comment_id"] = start_comment_id
        if offset:
            params["offset"] = offset
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            if count > 100:
                raise InvalidCountError(count, 100)
            params["count"] = count

        if sort == 1:
            params["sort"] = "asc"
        elif sort == -1:
            params["sort"] = "desc"
        else:
            raise UndefinedParameterValue("sort", sort)

        if preview_length:
            if preview_length < 0:
                raise NegativeValueError("preview_length", preview_length)
            params["preview_length"] = preview_length
        if extended:
            params["extended"] = True

            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str
        if comment_id is not None:
            if comment_id < 0:
                raise NegativeValueError("comment_id", comment_id)
            params["comment_id"] = comment_id
        if thread_items_count:
            params["thread_items_count"] = thread_items_count

        return self.request_async("wall.getComments", params)

    def get_reposts(self, owner_id: int, post_id: int,
                    offset: int = None, count: int = None):
        params = {"owner_id": owner_id, }

        if post_id <= 0:
            raise NegativeValueError("post_id", post_id)
        params["post_id"] = post_id

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        return self.request_async("wall.getReposts", params)

    def pin(self, owner_user_id: int, post_id: int):
        if post_id < 0:
            raise NegativeValueError("post_id", post_id)

        params = {
            "owner_id": owner_user_id,
            "post_id": post_id
        }
        return self.request_async("wall.pin", params)


class UsersMethods(SessionMixin):
    def search(self, text: str, sort: int = 0, offset: int = None, count: int = 100,
               fields: [ClubFields] = None, city: int = None, country: int = None,
               hometown: str = None, university_country: int = None, university: int = None,
               university_year: int = None, university_faculty: int = None,
               university_chair: int = None, sex: str | Sex = "any",
               status: int = None, age_from: int = None,
               age_to: int = None, birth_day: int = None, birth_month: int = None, birth_year: int = None,
               is_online: bool = False, has_photo: bool = False, school_country: int = None,
               school_city: int = None, school_class: int = None, school: int = None,
               school_year: int = None, religion: str = None, company: str = None,
               position: str = None, group_id: int = None, from_list: str = None,
               screen_ref: str = None):
        if sort and sort != 1:
            raise UndefinedParameterValue("sort", sort)

        params = {"q": text, "sort": sort}

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if count < 0:
            raise NegativeValueError("count", count)
        if fields:
            params["fields"] = ','.join(fields)
        if city:
            if city < 0:
                raise NegativeValueError("city", city)
            params["city"] = city
        if country:
            if country < 0:
                raise NegativeValueError("country", country)
            params["country"] = country
        if hometown:
            params["hometown"] = hometown
        if university_country:
            if university_country < 0:
                raise NegativeValueError("university_country", university_country)
            params["university_country"] = university_country
        if university:
            if university < 0:
                raise NegativeValueError("university", university)
            params["university"] = university
        if university_year:
            if university_year < 0:
                raise NegativeValueError("university_year", university_year)
            params["university_year"] = university_year
        if university_faculty:
            if university_faculty < 0:
                raise NegativeValueError("university_faculty", university_faculty)
            params["university_faculty"] = university_faculty
        if university_chair:
            if university_chair < 0:
                raise NegativeValueError("university_chair", university_chair)
            params["university_chair"] = university_chair

        match sex:
            case "any" | Sex.ANY:
                params["sex"] = 0
            case "male" | Sex.MALE:
                params["sex"] = 1
            case "female" | Sex.FEMALE:
                params["sex"] = 2
            case _:
                raise UndefinedParameterValue("sex", sex)

        if status is not None:
            if 1 <= status <= 8:
                params["status"] = status
            else:
                raise UndefinedParameterValue("status", status)
        if age_from:
            if age_from < 0:
                raise NegativeValueError("age_from", age_from)
            params["age_from"] = age_from
        if age_to:
            if age_to < 0:
                raise NegativeValueError("age_to", age_to)
            params["age_to"] = age_to
        if birth_day:
            if birth_day < 0:
                raise NegativeValueError("birth_day", birth_day)
            params["birth_day"] = birth_day
        if birth_month:
            if birth_month < 0:
                raise NegativeValueError("birth_month", birth_month)
            params["birth_month"] = birth_month
        if birth_year:
            if birth_year < 0:
                raise NegativeValueError("birth_year", birth_year)
            params["birth_year"] = birth_year
        if is_online:
            params["online"] = 1
        else:
            params["online"] = 0
        if has_photo:
            params["has_photo"] = 1
        else:
            params["has_photo"] = 0
        if school_country:
            if school_country < 0:
                raise NegativeValueError("school_country", school_country)
            params["school_country"] = school_country
        if school_city:
            if school_city < 0:
                raise NegativeValueError("school_city", school_city)
            params["school_city"] = school_city
        if school_class:
            if school_class < 0:
                raise NegativeValueError("school_class", school_class)
            params["school_class"] = school_class
        if school:
            if school < 0:
                raise NegativeValueError("school", school)
            params["school"] = school
        if school_year:
            if school_year < 0:
                raise NegativeValueError("school_year", school_year)
            params["school_year"] = school_year
        if religion:
            params["religion"] = religion
        if company:
            params["company"] = company
        if position:
            params["position"] = position
        if group_id:
            params["group_id"] = group_id
        if from_list:
            params["from_list"] = from_list
        if screen_ref:
            params["screen_ref"] = screen_ref

        return self.request_async("users.search", params)

    def get(self, user_ids: list, fields: list[UserFields] = None, name_case: str = "nom",
            from_group_id: int = None):
        params = {"user_ids": ','.join(user_ids)}
        if fields:
            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str
        if name_case in ["nom", "gen", "dat", "acc", "ins", "abl"]:
            params["name_case"] = name_case
        else:
            raise UndefinedParameterValue("name_case", name_case)
        if from_group_id:
            params["from_group_id"] = from_group_id

        return self.request_async("users.get", params)

    def get_followers(self, user_id: int, offset: int = None, count: int = None,
                      fields: list[UserFields] = None, name_case: str = "nom"):
        params = {
            "user_id": user_id
        }

        if offset < 0:
            raise NegativeValueError("offset", offset)
        if count < 0:
            raise NegativeValueError("count", count)
        params["offset"] = offset
        params["count"] = count

        if fields:
            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str

        if name_case in ["nom", "gen", "dat", "acc", "ins", "abl"]:
            params["name_case"] = name_case
        else:
            raise UndefinedParameterValue("name_case", name_case)

        return self.request_async("users.getFollowers", params)

    def get_my_followers(self, offset: int = None, count: int = None,
                         fields: list[UserFields] = None, name_case: str = "nom"):
        params = {}

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset
        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        if fields:
            fields_str = ""
            for field in fields:
                fields_str += ',' if fields_str else None
                fields_str += str(field)
            params["fields"] = fields_str

        if name_case in ["nom", "gen", "dat", "acc", "ins", "abl"]:
            params["name_case"] = name_case
        else:
            raise UndefinedParameterValue("name_case", name_case)

        return self.request_async("users.getFollowers", params)

    def report(self, user_id: int, report_type: str, comment: str = None):
        params = {
            "user_id": user_id,
            "type": report_type
        }

        if comment:
            params["comment"] = comment

        return self.request_async("users.report", params)


class GiftsMethods(SessionMixin):
    def get(self, user_id: int, count: int = None, offset: int = None) -> Coroutine[Any, Any, list[GiftItem]]:
        params = {
            "user_id": user_id
        }

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        return self.request_async("gifts.get", params)

    def get_my(self, count: int = None, offset: int = None) -> Coroutine[Any, Any, list[GiftItem]]:
        params = {}

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count
        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        return self.request_async("gifts.get", params)

