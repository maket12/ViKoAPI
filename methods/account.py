import datetime
from typing import Coroutine, Any, Tuple
from core.session_mixin import SessionMixin
from enums.account.sex import Sex
from enums.account.relation import RelationStatus
from enums.account.birthday_visibility import BirthdayVisibility
from vk_types.user.User import User
from vk_types.group.Group import Group
from errors.exceptions import *


class AccountMethods(SessionMixin):
    def ban(self, user_id: int) -> Coroutine[Any, Any, None]:
        """
        Adds the user or the group into the black list.\n
        Source: https://dev.vk.com/ru/method/account.ban.

        :param user_id: id of user or group
        :return: None
        """
        params = {"owner_id": user_id}
        return self.request_async("account.ban", params)

    def unban(self, user_id: int) -> Coroutine[Any, Any, None]:
        """
        Removes the user or the group from the black list.\n
        Source: https://dev.vk.com/ru/method/account.unban.

        :param user_id: id of user or group
        :return: None
        """
        params = {"owner_id": user_id}
        return self.request_async("account.unban", params)

    def set_online(self, voip: bool | None) -> Coroutine[Any, Any, None]:
        """
        Marks the current user as online for 5 minutes.\n
        Source: https://dev.vk.com/ru/method/account.setOnline.

        :param voip: Video calls enabled
        :return: None
        """
        params = {"voip": voip}
        return self.request_async("account.set_online", params)

    def set_offline(self) -> Coroutine[Any, Any, None]:
        """
        Marks the current user as offline.\n
        Source: https://dev.vk.com/ru/method/account.setOffline.

        :return: None
        """
        return self.request_async("account.set_offline", {})

    def edit(self,
             first_name: str | None,
             last_name: str | None,
             maiden_name: str | None,
             screen_name: str | None,
             sex: Sex | int | None,
             relation: RelationStatus | int | None,
             relation_user_id: int | None,
             birthday: datetime.datetime | None,
             birthday_visibility: BirthdayVisibility | int | None,
             home_town: str | None,
             country_id: int | None,
             city_id: int | None,
             status: str | None) -> Coroutine[Any, Any, None]:
        """
        Changes profile info of current account.\n
        Source: https://dev.vk.com/ru/method/account.saveProfileInfo.

        :param first_name: Capitalized first name
        :param last_name: Capitalized last name
        :param maiden_name: Capitalized maiden name (for women only)
        :param screen_name: Short link
        :param sex: Sex of user
        :param relation: Relation of user
        :param relation_user_id: Related user id
        :param birthday: Birth date
        :param birthday_visibility: How others see the birthdate
        :param home_town: Name of hometown
        :param country_id: ID of the country
        :param city_id: ID of the city
        :param status: the same as ``status.set``
        :return: None
        """
        if not first_name[0].isupper():
            raise ViKoAPIError("First name has to be capitalized.")
        if not last_name[0].isupper():
            raise ViKoAPIError("Second name has to be capitalized")
        if not maiden_name[0].isupper():
            raise ViKoAPIError("Maiden name has to be capitalized")
        if country_id <= 0:
            raise NegativeValueError("country_id", country_id)
        if city_id <= 0:
            raise NegativeValueError("city_id", city_id)

        params = {
            "first_name": first_name,
            "last_name": last_name,
            "maiden_name": maiden_name,
            "screen_name": screen_name,
            "sex": sex.value if isinstance(sex, Sex) else sex,
            "relation": relation.value if isinstance(relation, RelationStatus) else relation,
            "relation_partner_id": relation_user_id,
            "bdate": birthday.strftime("%d.%m.%Y") if birthday is not None else None,
            "bdate_visibility": birthday_visibility.value if isinstance(birthday_visibility, BirthdayVisibility) else None,
            "home_town": home_town,
            "country_id": country_id,
            "city_id": city_id,
            "status": status
        }

        return self.request_async("account.saveProfileInfo", params)

    def get_black_list(self,
                       offset: int | None,
                       count: int | None
                       ) -> Coroutine[Any, Any, Tuple[list[User], list[Group]]]:
        """
        Returns all users from the black list.\n
        Source: https://dev.vk.com/ru/method/account.getBanned.

        :param offset: Offset
        :param count: Amount of items to return
        :return: If there is only users/groups in the black list the only one data list will be returned. Otherwise, tuple of 2 data lists will  be returned.
        """
        if offset < 0:
            raise NegativeValueError("offset", offset)
        if count < 0:
            raise NegativeValueError("count", count)

        params = {"offset": offset, "count": count}

        return self.request_async("account.getBanned", params)
