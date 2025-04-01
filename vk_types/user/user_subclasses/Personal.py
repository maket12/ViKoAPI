from enums.user.political_views import PoliticalViews
from enums.user.people_main import PeopleMain
from enums.user.life_main import LifeMain
from enums.user.smoking import Smoking
from enums.user.alcohol import Alcohol


class UsersPersonal:
    def __init__(self, political: PoliticalViews | None, langs: list[str] | None, religion: str | None,
                 inspired_by: str | None, people_main: PeopleMain | None,
                 life_main: LifeMain | None, smoking: Smoking | None, alcohol: Alcohol | None):
        self.political = political
        self.langs = langs
        self.religion = religion
        self.inspired_by = inspired_by
        self.people_main = people_main
        self.life_main = life_main
        self.smoking = smoking
        self.alcohol = alcohol
