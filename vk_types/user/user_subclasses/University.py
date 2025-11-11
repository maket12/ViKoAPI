class UsersUniversity:
    def __init__(self, university_id: int | None, country_id: int | None,
                 city_id: int | None, name: str,
                 faculty_id: int | None, faculty_name: str | None, chair_id: int | None,
                 chair_name: str | None, graduation: int | None, education_form: str | None,
                 education_status: str | None):
        """
        Represents user.university object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param university_id:
        :param country_id:
        :param city_id:
        :param name:
        :param faculty_id:
        :param faculty_name:
        :param chair_id:
        :param chair_name:
        :param graduation:
        :param education_form:
        :param education_status:
        """
        self.university_id = university_id
        self.country_id = country_id
        self.city_id = city_id
        self.name = name
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.chair_id = chair_id
        self.chair_name = chair_name
        self.graduation = graduation
        self.education_form = education_form
        self.education_status = education_status

    def to_dict(self) -> dict:
        return {
            "id": self.university_id,
            "country": self.country_id,
            "city": self.city_id,
            "name": self.name,
            "faculty": self.faculty_id,
            "faculty_name": self.faculty_name,
            "chair": self.chair_id,
            "chair_name": self.chair_name,
            "graduation": self.graduation,
            "education_form": self.education_form,
            "education_status": self.education_status
        }
