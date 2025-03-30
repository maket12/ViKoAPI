from typing import Coroutine, Any, Tuple
from core.session_mixin import SessionMixin
from enums.user.fields import UserFields
from enums.group.fields import GroupFields
from enums.user.sex import Sex
from enums.user.report_type import ReportType
from vk_types.user.User import User
from vk_types.group.Group import Group
from errors.exceptions import *


class UsersMethods(SessionMixin):
    def get(self, user_ids: list, fields: list[UserFields] = None, name_case: str = "nom",
            from_group_id: int = None) -> Coroutine[Any, Any, list[User]]:
        params = {}

        for uid in user_ids:
            if uid <= 0:
                raise InvalidUserID(uid)
            params["user_ids"] += f",{uid}" if len(params["user_ids"]) != 0 else uid

        if fields:
            params["fields"] = ','.join(field.value for field in fields)

        if name_case in ["nom", "gen", "dat", "acc", "ins", "abl"]:
            params["name_case"] = name_case
        else:
            raise UndefinedParameterValue("name_case", name_case)

        if from_group_id:
            params["from_group_id"] = from_group_id

        return self.request_async("users.get", params)

    def search(self, text: str, sort: int = 0, offset: int = None, count: int = 100,
               fields: list[UserFields] = None, city: int = None, country: int = None,
               hometown: str = None, university_country: int = None, university: int = None,
               university_year: int = None, university_faculty: int = None,
               university_chair: int = None, sex: str | Sex = "any",
               status: int = None, age_from: int = None,
               age_to: int = None, birth_day: int = None, birth_month: int = None, birth_year: int = None,
               is_online: bool = False, has_photo: bool = False, school_country: int = None,
               school_city: int = None, school_class: int = None, school: int = None,
               school_year: int = None, religion: str = None, company: str = None,
               position: str = None, group_id: int = None, from_list: str = None,
               screen_ref: str = None) -> Coroutine[Any, Any, list[User]]:
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
            params["fields"] = ','.join(field.value for field in fields)
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

        params["online"] = is_online
        params["has_photo"] = has_photo

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

    def get_followers(self, user_id: int, offset: int | None = None, count: int | None = None,
                      fields: list[UserFields] | None = None,
                      name_case: str = "nom") -> Coroutine[Any, Any, list[User]]:
        if user_id <= 0:
            raise InvalidUserID(user_id)

        params = {
            "user_id": user_id
        }

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        if fields:
            params["fields"] = ','.join(field.value for field in fields)

        if name_case in ["nom", "gen", "dat", "acc", "ins", "abl"]:
            params["name_case"] = name_case
        else:
            raise UndefinedParameterValue("name_case", name_case)

        return self.request_async("users.getFollowers", params)

    def get_my_followers(self, offset: int | None = None, count: int | None = None,
                         fields: list[UserFields] | None = None,
                         name_case: str = "nom") -> Coroutine[Any, Any, list[User]]:
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
            params["fields"] = ','.join(field.value for field in fields)

        if name_case in ["nom", "gen", "dat", "acc", "ins", "abl"]:
            params["name_case"] = name_case
        else:
            raise UndefinedParameterValue("name_case", name_case)

        return self.request_async("users.getFollowers", params)

    def get_subscriptions(
            self, user_id: int, offset: int | None = None, count: int | None = None,
            fields: list[UserFields | GroupFields] | None = None
    ) -> Coroutine[Any, Any, Tuple[list[User], list[Group]]]:
        if user_id <= 0:
            raise InvalidUserID(user_id)
        params = {"user_id": user_id}

        if offset:
            if offset < 0:
                raise NegativeValueError("offset", offset)
            params["offset"] = offset

        if count:
            if count < 0:
                raise NegativeValueError("count", count)
            params["count"] = count

        if fields:
            params["fields"] = ','.join(str(field.value) for field in fields)

        return self.request_async("users.getSubscriptions", params)

    def report(self, user_id: int, report_type: ReportType | str,
               comment: str | None = None) -> Coroutine[Any, Any, None]:
        if user_id <= 0:
            raise InvalidUserID(user_id)

        params = {
            "user_id": user_id,
        }

        if isinstance(report_type, ReportType):
            params["type"] = report_type.value
        else:
            params["type"] = report_type

        if comment:
            params["comment"] = comment

        return self.request_async("users.report", params)
