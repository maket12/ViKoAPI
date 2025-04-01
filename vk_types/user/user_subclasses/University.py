class UsersUniversity:
    def __init__(self, university_id: int | None, city_id: int | None, name: str,
                 faculty_id: int | None, faculty_name: str | None, chair_id: int | None,
                 chair_name: str | None, graduation: int | None, education_form: str | None,
                 education_status: str | None):
        self.university_id = university_id
        self.city_id = city_id
        self.name = name
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.chair_id = chair_id
        self.chair_name = chair_name
        self.graduation = graduation
        self.education_form = education_form
        self.education_status = education_status
