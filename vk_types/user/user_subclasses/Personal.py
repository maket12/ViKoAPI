from enums.user.political_views import PoliticalViews
from enums.user.people_main import PeopleMain
from enums.user.life_main import LifeMain
from enums.user.smoking import Smoking
from enums.user.alcohol import Alcohol


class UsersPersonal:
    def __init__(self, political: PoliticalViews | None, langs: list[str] | None, religion: str | None,
                 inspired_by: str | None, people_main: PeopleMain | None,
                 life_main: LifeMain | None, smoking: Smoking | None, alcohol: Alcohol | None):
        """
        Represents user.personal object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param political:
        :param langs:
        :param religion:
        :param inspired_by:
        :param people_main:
        :param life_main:
        :param smoking:
        :param alcohol:
        """
        self.political = political
        self.langs = langs
        self.religion = religion
        self.inspired_by = inspired_by
        self.people_main = people_main
        self.life_main = life_main
        self.smoking = smoking
        self.alcohol = alcohol

    def to_dict(self) -> dict:
        return {
            "political": self.political.value if self.political is not None else None,
            "langs": self.langs,
            "religion": self.religion,
            "inspired_by": self.inspired_by,
            "people_main": self.people_main.value if self.people_main is not None else None,
            "life_main": self.life_main.value if self.life_main is not None else None,
            "smoking": self.smoking.value if self.smoking is not None else None,
            "alcohol": self.alcohol.value if self.alcohol is not None else None
        }
