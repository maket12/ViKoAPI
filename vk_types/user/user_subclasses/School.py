from enums.user.school_type import SchoolType


class UsersSchool:
    def __init__(self, school_id: int | None, country_id: int | None,
                 city_id: int | None, name: str, year_from: int | None,
                 year_to: int | None, year_graduated: int | None, class_letter: str | None,
                 speciality: str | None, school_type: SchoolType):
        """
        Represents user.school object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param school_id:
        :param country_id:
        :param city_id:
        :param name:
        :param year_from:
        :param year_to:
        :param year_graduated:
        :param class_letter:
        :param speciality:
        :param school_type:
        """
        self.school_id = school_id
        self.country_id = country_id
        self.city_id = city_id
        self.name = name
        self.year_from = year_from
        self.year_to = year_to
        self.year_graduated = year_graduated
        self.class_letter = class_letter
        self.speciality = speciality
        self.school_type = school_type

    def to_dict(self) -> dict:
        return {
            "id": self.school_id,
            "country": self.country_id,
            "city": self.city_id,
            "name": self.name,
            "year_from": self.year_from,
            "year_to": self.year_to,
            "year_graduated": self.year_graduated,
            "class": self.class_letter,
            "speciality": self.speciality,
            "type": self.school_type.value,
        }
