class UsersEducation:
    def __init__(self, university: int, university_name: str, faculty: int,
                 faculty_name: str, graduation: int):
        """
        Represents user.education object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param university: ID of the university
        :param university_name: Name of the university
        :param faculty: ID of the faculty
        :param faculty_name: Name of the faculty
        :param graduation: Year of graduation
        """
        self.university = university
        self.university_name = university_name
        self.faculty = faculty
        self.faculty_name = faculty_name
        self.graduation = graduation

    def to_dict(self) -> dict:
        return {
            "university": self.university,
            "university_name": self.university_name
        }
