class UsersSurnameCases:
    def __init__(self, surname_in_nom: str | None, surname_in_gen: str | None, surname_in_dat: str | None,
                 surname_in_acc: str | None, surname_in_ins: str | None, surname_in_abl: str | None):
        """
        Represents user.last_name_cases object.\n
        Source: https://dev.vk.com/ru/reference/objects/user.

        :param surname_in_nom:
        :param surname_in_gen:
        :param surname_in_dat:
        :param surname_in_acc:
        :param surname_in_ins:
        :param surname_in_abl:
        """
        self.surname_in_nom = surname_in_nom
        self.surname_in_gen = surname_in_gen
        self.surname_in_dat = surname_in_dat
        self.surname_in_acc = surname_in_acc
        self.surname_in_ins = surname_in_ins
        self.surname_in_abl = surname_in_abl

    def to_dict(self) -> dict:
        return {
            "nom": self.surname_in_nom,
            "gen": self.surname_in_gen,
            "dat": self.surname_in_dat,
            "acc": self.surname_in_acc,
            "ins": self.surname_in_ins,
            "abl": self.surname_in_abl
        }
