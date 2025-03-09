from enums.user.school_type import SchoolType


class UsersSchool:
    def __init__(self, school_id: int | None, city_id: int | None, name: str, year_from: int | None,
                 year_to: int | None, year_graduated: int | None, class_letter: str | None,
                 speciality: str | None, school_type: SchoolType):
        self.school_id = school_id
        self.city_id = city_id
        self.name = name
        self.year_from = year_from
        self.year_to = year_to
        self.year_graduated = year_graduated
        self.class_letter = class_letter
        self.speciality = speciality
        self.school_type = school_type
